class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.skills = None or []

    def learn_skill(self, skill: str) -> None:
        return self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.default_skills = ["JavaScript", "HTML", "CSS"]
        self.skills.extend(self.default_skills)

    def create_awesome_web_page(self) -> str:
        print(self.name, "is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.default_skills = ["Python", "SQL", "Django"]
        self.skills.extend(self.default_skills)

    def create_powerful_api(self) -> str:
        print(self.name, "is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.default_skills = ["Java", "Android studio"]
        self.skills.extend(self.default_skills)

    def create_smooth_mobile_app(self) -> str:
        print(self.name, "is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):

    def create_web_application(self) -> None:
        print(self.name, "started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()


if __name__ == "__main__":
    engineer = SoftwareEngineer("Max")
    front_dev = FrontendDeveloper("Alisa")
    backend_dev = BackendDeveloper("Bob")
    android_dev = AndroidDeveloper("Beth")
    full_stack_dev = FullStackDeveloper("Tom")
    engineer.learn_skill("Python")

    print(backend_dev.skills)
    print()
    print(engineer.skills)
    print()
    print(front_dev.default_skills)
    print()
    front_dev.create_awesome_web_page()
    print(front_dev.create_awesome_web_page())
    print()
    print(backend_dev.create_powerful_api())
    print()
    print(android_dev.create_smooth_mobile_app())
    print()
    full_stack_dev.create_web_application()
