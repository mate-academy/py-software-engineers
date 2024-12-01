from typing import List


class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.skills: List[str] = []

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(["JavaScript", "HTML", "CSS"])

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(["Python", "SQL", "Django"])

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(["Java", "Android studio"])

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    def __init__(self, name: str) -> None:
        FrontendDeveloper.__init__(self, name)
        BackendDeveloper.__init__(self, name)

        self.skills = list(
            sorted(
                set(self.skills),
                key=lambda x: [
                    "Python", "SQL", "Django", "JavaScript", "HTML", "CSS"
                ].index(x)
            )
        )

    def create_web_application(self) -> str:
        messages = []
        messages.append(f"{self.name} started creating a web application...")
        messages.append(self.create_powerful_api())
        messages.append(self.create_awesome_web_page())
        return "\n".join(messages)


full_stack_dev = FullStackDeveloper("Tom")
print(full_stack_dev.create_web_application())
