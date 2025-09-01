from models import User

def autenticar_usuario(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return True
    return False
<<<<<<< HEAD:utils.py
=======

>>>>>>> 049ad2247eab6cf7880927b972c46d30af2df293:proyecto railways/utils.py
