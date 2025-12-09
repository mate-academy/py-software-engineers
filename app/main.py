class SoftwareEngineer:
    def __init__(self, name) -> None:
        self.name = name
        self.skills = []

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class FrontEnd(SoftwareEngineer):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.learn_skill("JavaScript")
        self.learn_skill("HTML")
        self.learn_skill("CSS")

    def create_awesome_web_page(self) -> str:
        message = f"{self.name} is creating a webpage..."
        print(message)
        return "<h1>Hello world</h1>"


class BackEnd(SoftwareEngineer):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.learn_skill("Python")
        self.learn_skill("SQL")
        self.learn_skill("Django")

    def create_powerful_api(self) -> str:
        message = f"{self.name} is creating an API..."
        print(message)
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.learn_skill("Java")
        self.learn_skill("Android studio")

    def create_smooth_mobile_app(self) -> str:
        message = f"{self.name} is creating a mobile app..."
        print(message)
        return "Ads every three swipes"


class FullStackDeveloper(FrontEnd, BackEnd):
    def __init__(self, name) -> None:
        super().__init__(name)

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
