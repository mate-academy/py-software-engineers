import io
from contextlib import redirect_stdout
import pytest

from app.main import (
    SoftwareEngineer,
    FrontendDeveloper,
    BackendDeveloper,
    FullStackDeveloper,
    AndroidDeveloper,
)


def test_code_method():
    engineer = SoftwareEngineer("Alisa")
    f = io.StringIO()
    with redirect_stdout(f):
        engineer.code()
    assert f.getvalue() == "Alisa is coding...\n"


def test_learn_skills_method():
    engineer = SoftwareEngineer("Bob")
    engineer.learn_skills("Python", "Django")
    assert "Python" in engineer.skills
    assert "Django" in engineer.skills


@pytest.mark.parametrize(
    "engineer,printed_message",
    [
        (FrontendDeveloper("Alisa"), "Alisa is creating a webpage...\n"),
        (FullStackDeveloper("Bob"), "Bob is creating a webpage...\n"),
    ]
)
def test_create_awesome_web_page_method(engineer, printed_message):
    f = io.StringIO()
    with redirect_stdout(f):
        assert engineer.create_awesome_web_page() == "<h1>Hello world</h1>"
    assert f.getvalue() == printed_message


@pytest.mark.parametrize(
    "engineer,printed_message",
    [
        (BackendDeveloper("Alisa"), "Alisa is creating an API...\n"),
        (FullStackDeveloper("Bob"), "Bob is creating an API...\n"),
    ]
)
def test_create_powerful_api_method(engineer, printed_message):
    f = io.StringIO()
    with redirect_stdout(f):
        assert engineer.create_powerful_api() == "http://127.0.0.1:8000"
    assert f.getvalue() == printed_message


@pytest.mark.parametrize(
    "engineer,printed_message",
    [
        (AndroidDeveloper("Alisa"), "Alisa is creating a mobile app...\n"),
        (AndroidDeveloper("Bob"), "Bob is creating a mobile app...\n"),
    ]
)
def test_create_smooth_mobile_app_method(engineer, printed_message):
    f = io.StringIO()
    with redirect_stdout(f):
        assert engineer.create_smooth_mobile_app() == "Ads every three swipes"
    assert f.getvalue() == printed_message


def test_create_web_application_method():
    dev = FullStackDeveloper("Charlie")
    result = dev.create_web_application()
    assert result == {
        "frontend": "<h1>Hello world</h1>",
        "backend": "http://127.0.0.1:8000",
    }
