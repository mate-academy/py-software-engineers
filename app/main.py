from __future__ import annotations


class SoftwareEngineer:
    def __init__(
            self,
            name: str,
    ) -> None:
        self.name = name
        self.skills: list[str] = []

    def learn_skill(
            self,
            skill: str
    ) -> None:
        if skill not in self.skills:
            self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    FRONTEND_SKILLS = ("JavaScript", "HTML", "CSS")

    def __init__(
            self,
            name: str,
    ) -> None:
        super().__init__(name)
        self.skills.extend(self.FRONTEND_SKILLS)

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    BACKEND_SKILLS = ("Python", "SQL", "Django")

    def __init__(
            self,
            name: str,
    ) -> None:
        super().__init__(name)
        self.skills.extend(self.BACKEND_SKILLS)

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    ANDROID_SKILLS = ("Java", "Android studio")

    def __init__(
            self,
            name: str
    ) -> None:
        super().__init__(name)
        self.skills.extend(self.ANDROID_SKILLS)

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
