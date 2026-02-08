class SoftwareEngineer:
    def __init__(self, name: str,) -> None:
        self.name = name
        self.skills = []

    def learn_skill(self, skill: str) -> None:
        if skill not in self.skills:
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

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()

if __name__ == "__main__":
    frontend_dev = FrontendDeveloper("Alice")
    backend_dev = BackendDeveloper("Bob")
    android_dev = AndroidDeveloper("Charlie")
    fullstack_dev = FullStackDeveloper("Dave")

    print(f"{frontend_dev.name} skills: {frontend_dev.skills}")
    print(f"{backend_dev.name} skills: {backend_dev.skills}")
    print(f"{android_dev.name} skills: {android_dev.skills}")
    print(f"{fullstack_dev.name} skills: {fullstack_dev.skills}")

    frontend_dev.create_awesome_web_page()
    backend_dev.create_powerful_api()
    android_dev.create_smooth_mobile_app()
    fullstack_dev.create_web_application()