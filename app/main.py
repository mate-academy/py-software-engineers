class SoftwareEngineer:
    def __init__(self, name: str): -> None:
        self.name = name
        self.skills = []

    def learn_skills(self, skill: str) -> None:
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer) -> None:
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(["JavaScript", "HTML", "CSS"])

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello World</h1>"

class BackendDeveloper(SoftwareEngineer) -> None:
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(["PythonL", "SQL", "Django"])

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating a powerful API...")
        return "http://127.0.0.1:8000/"


class AndroidDeveloper(SoftwareEngineer) -> None:
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(["Java", "Android Studio"])

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
