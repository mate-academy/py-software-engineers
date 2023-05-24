class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self._name: str = name
        self._skills: list[str] = []

    def learn_skill(self, skill: str) -> None:
        if skill in self._skills:
            return
        self._skills.append(skill)

    def _learn_skills(self, *skills) -> None:
        self._skills.extend((skill for skill in skills
                             if isinstance(skill, str)
                             and skill not in self._skills))

    @property
    def name(self) -> str:
        return self._name

    @property
    def skills(self) -> list[str]:
        return self._skills[:]


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._learn_skills("JavaScript", "HTML", "CSS")

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._learn_skills("Python", "SQL", "Django")

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._learn_skills("Java", "Android studio")

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
