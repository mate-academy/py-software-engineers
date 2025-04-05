import io
from contextlib import redirect_stdout
import typing
from app.main import (
    SoftwareEngineer,
    FrontendDeveloper,
    BackendDeveloper,
    AndroidDeveloper,
    FullStackDeveloper,
)


def test_code_method():
    engineer = SoftwareEngineer("Alisa")
    f = io.StringIO()
    with redirect_stdout(f):
        engineer.code()
    assert f.getvalue() == "Alisa is coding...\n"


def test_learn_skill_method():
    engineer = SoftwareEngineer("Bob")
    engineer.learn_skill("Python")
    engineer.learn_skill("Django")
    assert "Python" in engineer.skills
    assert "Django" in engineer.skills


def test_create_awesome_web_page():
    dev = FrontendDeveloper("Jane")
    f = io.StringIO()
    with redirect_stdout(f):
        result = dev.create_awesome_web_page()
    assert result == "<h1>Hello world</h1>"
    assert f.getvalue() == "Jane is creating a webpage...\n"


def test_create_powerful_api():
    dev = BackendDeveloper("Max")
    f = io.StringIO()
    with redirect_stdout(f):
        result = dev.create_powerful_api()
    assert result == "http://127.0.0.1:8000"
    assert f.getvalue() == "Max is creating an API...\n"


def test_create_smooth_mobile_app():
    dev = AndroidDeveloper("Anna")
    f = io.StringIO()
    with redirect_stdout(f):
        result = dev.create_smooth_mobile_app()
    assert result == "Ads every three swipes"
    assert f.getvalue() == "Anna is creating a mobile app...\n"


def test_create_web_application_method():
    dev = FullStackDeveloper("Charlie")
    f = io.StringIO()
    with redirect_stdout(f):
        result = dev.create_web_application()
    assert result == "<React + Django + PostgreSQL>"
    assert f.getvalue() == "Charlie is creating a web application...\n"


def test_type_annotations():
    functions = [
        SoftwareEngineer.code,
        SoftwareEngineer.learn_skill,
        FrontendDeveloper.create_awesome_web_page,
        BackendDeveloper.create_powerful_api,
        AndroidDeveloper.create_smooth_mobile_app,
        FullStackDeveloper.create_web_application,
    ]
    for function in functions:
        hints = typing.get_type_hints(function)
        result = {k: v for k, v in hints.items()}
        assert dict(hints) == result, "Add or fix type annotation for methods"
