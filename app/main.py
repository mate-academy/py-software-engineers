class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.skills = []
        self.name = name

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(["JavaScript", "CSS", "HTML"])

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        webpage = "<h1>Hello world</h1>"
        return webpage


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(["Python", "SQL", "Django"])

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        api_address = "http://127.0.0.1:8000"
        return api_address


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(["Java", "Android studio"])

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        app_ux = "Ads every three swipes"
        return app_ux


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
