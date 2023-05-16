class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.skills: list[str] = []

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):

    skills: list[str] = ["JavaScript", "HTML", "CSS"]

    def __init__(self, name: str) -> None:
        super().__init__(name=name)
        self.skills += ["JavaScript", "HTML", "CSS"]

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):

    skills: list[str] = ["Python", "SQL", "Django"]

    def __init__(self, name: str) -> None:
        super().__init__(name=name)
        self.skills += ["Python", "SQL", "Django"]

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):

    skills: list[str] = ["Java", "Android studio"]

    def __init__(self, name: str) -> None:
        super().__init__(name=name)
        self.skills += ["Java", "Android studio"]

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    def __init__(self, name: str) -> None:
        super().__init__(name=name)
        self.skills += ["JavaScript", "HTML", "CSS"]

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        super().create_powerful_api()
        super().create_awesome_web_page()



i1 = SoftwareEngineer("", ["AWS", "Docker"])


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