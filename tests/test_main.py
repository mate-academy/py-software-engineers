import io
from contextlib import redirect_stdout

import pytest
import typing
from typing import Callable

from app.main import SoftwareEngineer, FrontendDeveloper, BackendDeveloper, FullStackDeveloper, AndroidDeveloper


@pytest.mark.parametrize(
    "class_,methods",
    [
        (SoftwareEngineer, ["__init__", "learn_skill"]),
        (FrontendDeveloper, ["__init__", "learn_skill", "create_awesome_web_page"]),
        (BackendDeveloper, ["__init__", "learn_skill", "create_powerful_api"]),
        (AndroidDeveloper, ["__init__", "learn_skill", "create_smooth_mobile_app"]),
        (FullStackDeveloper, ["__init__", "learn_skill", "create_powerful_api", "create_awesome_web_page"]),
    ],
)
def test_classes_should_have_corresponding_methods(class_, methods):
    for method in methods:
        assert (
                hasattr(class_, method) is True
        ), f"Class '{class_.__name__}' should have method {method}"


@pytest.mark.parametrize(
    "engineer,default_skills",
    [
        (SoftwareEngineer(""), []),
        (FrontendDeveloper(""), ["JavaScript", "CSS", "HTML"]),
        (BackendDeveloper(""), ["Python", "SQL", "Django"]),
        (FullStackDeveloper(""), ["Python", "SQL", "Django", "JavaScript", "CSS", "HTML"]),
        (AndroidDeveloper(""), ["Java", "Android studio"]),
    ]
)
def test_default_skills(engineer, default_skills):
    assert sorted(engineer.skills) == sorted(default_skills)


@pytest.mark.parametrize(
    "engineer,new_skills,final_skill_list",
    [
        (SoftwareEngineer(""), ["AWS", "Docker"], ["AWS", "Docker"]),
        (FrontendDeveloper(""), ["TypeScript", "React"], ["JavaScript", "CSS", "HTML", "TypeScript", "React"]),
        (BackendDeveloper(""), ["Golang"], ["Python", "SQL", "Django", "Golang"]),
        (FullStackDeveloper(""), ["AWS", "React"],
         ["Python", "SQL", "Django", "JavaScript", "CSS", "HTML", "AWS", "React"]),
        (AndroidDeveloper(""), ["Firebase"], ["Java", "Android studio", "Firebase"]),
    ]
)
def test_learn_skills_method(engineer, new_skills, final_skill_list):
    for skill in new_skills:
        engineer.learn_skill(skill)
    assert sorted(engineer.skills) == sorted(final_skill_list)


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


@pytest.mark.parametrize(
    "engineer,printed_messages",
    [
        (
            FullStackDeveloper("Alisa"),
            ("Alisa started creating a web application...\n"
             "Alisa is creating an API...\n"
             "Alisa is creating a webpage...\n")
        ),
        (
                FullStackDeveloper("Bob"),
                ("Bob started creating a web application...\n"
                 "Bob is creating an API...\n"
                 "Bob is creating a webpage...\n")
        ),
    ]
)
def test_create_web_application_method(engineer, printed_messages):
    f = io.StringIO()
    with redirect_stdout(f):
        engineer.create_web_application()
    assert f.getvalue() == printed_messages


@pytest.mark.parametrize(
    "function,result",
    [
        (
                SoftwareEngineer.__init__,
                {"name": str,
                 "return": type(None)}
        ),
        (
                SoftwareEngineer.learn_skill,
                {"skill": str,
                 "return": type(None)}
        ),
        (
                FrontendDeveloper.__init__,
                {"name": str,
                 "return": type(None)}
        ),
        (
                FrontendDeveloper.create_awesome_web_page,
                {"return": str}
        ),
        (
                BackendDeveloper.__init__,
                {"name": str,
                 "return": type(None)}
        ),
        (
                BackendDeveloper.create_powerful_api,
                {"return": str}
        ),
        (
                AndroidDeveloper.__init__,
                {"name": str,
                 "return": type(None)}
        ),
        (
                AndroidDeveloper.create_smooth_mobile_app,
                {"return": str}
        ),
        (
                FullStackDeveloper.__init__,
                {"name": str,
                 "return": type(None)}
        ),
        (
                FullStackDeveloper.create_web_application,
                {"return": type(None)}
        )
    ]
)
def test_added_type_annotation(function: Callable, result: dict) -> None:
    hints = typing.get_type_hints(function)
    assert dict(hints) == result, "Add or fix type annotation for methods"
