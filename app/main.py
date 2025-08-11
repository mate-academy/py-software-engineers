class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.skills = []

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    s_skills = ["JavaScript", "HTML", "CSS"]

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(FrontendDeveloper.s_skills)

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    s_skills = ["Python", "SQL", "Django"]

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(BackendDeveloper.s_skills)

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


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    def __init__(self, name: str) -> None:
        # That's how it was: super().__init__(name)
        # but, due to AI demands, I had to change all those 3 classes
        super().__init__(name)
        self.skills = BackendDeveloper.s_skills + FrontendDeveloper.s_skills

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()


if __name__ == "__main__":
    pass
