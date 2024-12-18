import pytest
from app.main import SoftwareEngineer, FrontendDeveloper, BackendDeveloper, FullStackDeveloper, AndroidDeveloper

@pytest.mark.parametrize(
    "engineer,new_skills,final_skill_list",
    [
        (SoftwareEngineer("Engineer1"), ["AWS", "Docker"], ["AWS", "Docker"]),
        (FrontendDeveloper("Engineer2"), ["TypeScript", "React"], ["JavaScript", "CSS", "HTML", "TypeScript", "React"]),
        (BackendDeveloper("Engineer3"), ["Golang"], ["Python", "SQL", "Django", "Golang"]),
        (FullStackDeveloper("Engineer4"), ["AWS", "React"], ["JavaScript", "CSS", "HTML", "Python", "SQL", "Django", "AWS", "React"]),
        (AndroidDeveloper("Engineer5"), ["Firebase"], ["Java", "Android Studio", "Firebase"]),
    ]
)
def test_learn_skills_method(engineer, new_skills, final_skill_list):
    for skill in new_skills:
        engineer.learn_skill(skill)
    assert sorted(engineer.skills) == sorted(final_skill_list)


@pytest.mark.parametrize(
    "engineer,default_skills",
    [
        (SoftwareEngineer("Engineer1"), []),
        (FrontendDeveloper("Engineer2"), ["JavaScript", "CSS", "HTML"]),
        (BackendDeveloper("Engineer3"), ["Python", "SQL", "Django"]),
        (FullStackDeveloper("Engineer4"), ["JavaScript", "CSS", "HTML", "Python", "SQL", "Django"]),
        (AndroidDeveloper("Engineer5"), ["Java", "Android Studio"]),
    ]
)
def test_default_skills(engineer, default_skills):
    assert sorted(engineer.skills) == sorted(default_skills)
