import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time
import subprocess
import sys
import os


@pytest.fixture(scope="module", autouse=True)
def start_flask_server():
    env = os.environ.copy()
    env["FLASK_ENV"] = "development"
    env["LOCAL_DB_URL"] = "sqlite:///test.db"
    proc = subprocess.Popen(
        [sys.executable, "run.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
    )
    time.sleep(5)
    yield
    proc.terminate()
    proc.wait()


@pytest.fixture(scope="module")
def browser():
    firefox_options = Options()
    firefox_options.add_argument("--headless")

    driver = webdriver.Firefox(options=firefox_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def logged_in_session(browser):
    browser.get("http://127.0.0.1:5000/login")
    browser.find_element(By.NAME, "username").send_keys("root")
    browser.find_element(By.NAME, "password").send_keys("root")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1)
    return browser


def test_navigate_to_socios(logged_in_session):
    browser = logged_in_session
    browser.get("http://127.0.0.1:5000/socios")
    assert "Socios" in browser.page_source or "socio" in browser.page_source.lower()
    print("PASS: Navigate to Socios")


def test_navigate_to_componentes(logged_in_session):
    browser = logged_in_session
    browser.get("http://127.0.0.1:5000/componentes")
    assert (
        "Componente" in browser.page_source
        or "componente" in browser.page_source.lower()
    )
    print("PASS: Navigate to Componentes")


def test_navigate_to_casos(logged_in_session):
    browser = logged_in_session
    browser.get("http://127.0.0.1:5000/casos")
    assert "Caso" in browser.page_source or "caso" in browser.page_source.lower()
    print("PASS: Navigate to Casos")


def test_navigate_to_usuarios(logged_in_session):
    browser = logged_in_session
    browser.get("http://127.0.0.1:5000/usuarios")
    assert "Usuario" in browser.page_source or "usuario" in browser.page_source.lower()
    print("PASS: Navigate to Usuarios")


def test_navigate_to_logs(logged_in_session):
    browser = logged_in_session
    browser.get("http://127.0.0.1:5000/logs")
    assert "Log" in browser.page_source or "log" in browser.page_source.lower()
    print("PASS: Navigate to Logs")


def test_navigate_to_dashboard(logged_in_session):
    browser = logged_in_session
    browser.get("http://127.0.0.1:5000/dashboard")
    assert "Dashboard" in browser.page_source or "Estad" in browser.page_source
    print("PASS: Navigate to Dashboard")
