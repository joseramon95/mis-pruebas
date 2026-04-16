import pytest
from app import create_app, db
from app.models import Usuario
import os


@pytest.fixture(scope="module")
def app():
    os.environ["FLASK_ENV"] = "development"
    os.environ["LOCAL_DB_URL"] = "sqlite:///test.db"
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

    with app.app_context():
        db.create_all()
        root = Usuario(username="root", rol="admin")
        root.set_password("root")
        db.session.add(root)
        db.session.commit()
        yield app
        db.drop_all()


@pytest.fixture(scope="module")
def client(app):
    return app.test_client()


@pytest.fixture(scope="function")
def authenticated_client(client):
    client.post("/login", data={"username": "root", "password": "root"})
    return client


def test_create_user(authenticated_client):
    response = authenticated_client.post(
        "/usuarios/nuevo",
        data={"username": "testuser", "password": "testpass123", "rol": "editor"},
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"testuser" in response.data or "testuser" in response.data.decode()


def test_delete_user(authenticated_client):
    client = authenticated_client

    with client.application.app_context():
        user = Usuario.query.filter_by(username="testuser").first()
        if user:
            user_id = user.id

    if user_id := locals().get("user_id"):
        response = client.post(f"/usuarios/eliminar/{user_id}", follow_redirects=True)
        assert response.status_code == 200


def test_create_and_delete_user_flow(authenticated_client):
    client = authenticated_client

    response = client.post(
        "/usuarios/nuevo",
        data={"username": "testuser2", "password": "testpass123", "rol": "editor"},
        follow_redirects=True,
    )

    with client.application.app_context():
        user = Usuario.query.filter_by(username="testuser2").first()
        assert user is not None
        user_id = user.id

    response = client.post(f"/usuarios/eliminar/{user_id}", follow_redirects=True)

    with client.application.app_context():
        user = Usuario.query.filter_by(username="testuser2").first()
        assert user is None
