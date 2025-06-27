from typing import List
import json

class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.skills: List[str] = []

    def __str__(self) -> str:
        return json.dumps({'name': self.name, 'skills': self.skills})

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(["JavaScript", "HTML", "CSS"])

    def create_awesome_web_page(self) -> str:
        return f"{self.name} is creating a webpage...\n<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(["Python", "SQL", "Django"])

    def create_powerful_api(self) -> str:
        return f"{self.name} is creating an API...\nhttp://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(["Java", "Android studio"])

    def create_smooth_mobile_app(self) -> str:
        return f"{self.name} is creating a mobile app...\nAds every three swipes"


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    def __init__(self, name: str) -> None:
        SoftwareEngineer.__init__(self, name)
        self.skills.extend([
            "Python", "SQL", "Django",
            "JavaScript", "HTML", "CSS"
        ])

    def create_web_application(self) -> str:
        return (
            f"{self.name} started creating a web application...\n"
            + self.create_powerful_api() + "\n"
            + self.create_awesome_web_page()
        )


if __name__ == "__main__":
    dev = FullStackDeveloper("Alice")
    print(dev)
    print(dev.create_web_application())
