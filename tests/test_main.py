import io
from contextlib import redirect_stdout
import pytest
from app.main import SoftwareEngineer, FrontendDeveloper, BackendDeveloper, FullStackDeveloper, AndroidDeveloper

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

@pytest.mark.parametrize(
    "engineer,printed_messages",
    [
        (
            FullStackDeveloper("Alisa"),
            "Alisa started creating a web application...\nAlisa is creating an API...\nAlisa is creating a webpage...\n"
        ),
        (
            FullStackDeveloper("Bob"),
            "Bob started creating a web application...\nBob is creating an API...\nBob is creating a webpage...\n"
        ),
    ]
)
def test_create_web_application_method(engineer, printed_messages):
    f = io.StringIO()
    with redirect_stdout(f):
        engineer.create_web_application()
    assert f.getvalue() == printed_messages

@pytest.mark.parametrize(
    "engineer,new_skills,final_skill_list",
    [
        (SoftwareEngineer(""), ["AWS", "Docker"], ["aws", "docker"]),
        (FrontendDeveloper(""), ["TypeScript", "React"], ["javascript", "css", "html", "typescript", "react"]),
        (BackendDeveloper(""), ["Golang"], ["python", "sql", "django", "golang"]),
        (FullStackDeveloper(""), ["AWS", "React"], ["python", "sql", "django", "javascript", "css", "html", "aws", "react"]),
        (AndroidDeveloper(""), ["Firebase"], ["java", "android studio", "firebase"]),
    ]
)
def test_learn_skills_method(engineer, new_skills, final_skill_list):
    for skill in new_skills:
        engineer.learn_skill(skill)
    assert sorted(engineer.skills) == sorted(final_skill_list)

@pytest.mark.parametrize(
    "engineer,default_skills",
    [
        (SoftwareEngineer(""), []),
        (FrontendDeveloper(""), ["javascript", "css", "html"]),
        (BackendDeveloper(""), ["python", "sql", "django"]),
        (FullStackDeveloper(""), ["python", "sql", "django", "javascript", "css", "html"]),
        (AndroidDeveloper(""), ["java", "android studio"]),
    ]
)
def test_default_skills(engineer, default_skills):
    assert sorted(engineer.skills) == sorted(default_skills)
