class SoftwareEngineer:

    def __init__(self, name: str) -> None:
        self.name = name
        self.skills = []

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(["JavaScript", "HTML", "CSS"])

    def create_awesome_web_page(self) -> str:
        message = f"{self.name} is creating a webpage..."
        page = "<h1>Hello world</h1>"
        print(message)
        return page


class BackendDeveloper(SoftwareEngineer):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(["Python", "SQL", "Django"])

    def create_powerful_api(self) -> str:
        message = f"{self.name} is creating an API..."
        api = "http://127.0.0.1:8000"
        print(message)
        return api


class AndroidDeveloper(SoftwareEngineer):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(["Java", "Android studio"])

    def create_smooth_mobile_app(self) -> str:
        message = f"{self.name} is creating a mobile app..."
        mobile = "Ads every three swipes"
        print(message)
        return mobile


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):

    def __init__(self, name: str) -> None:
        SoftwareEngineer.__init__(self, name)
        self.skills.extend(["Python", "SQL", "Django"])
        self.skills.extend(["JavaScript", "HTML", "CSS"])

    def create_web_application(self) -> None:
        message = f"{self.name} started creating a web application..."
        print(message)
        self.create_powerful_api()
        self.create_awesome_web_page()
