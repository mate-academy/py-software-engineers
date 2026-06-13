class SoftwareEngineer:

    def __init__(self, name: str, skills=None) -> None:
        if skills is None:
            skills = []
        self.name = name
        self.skills = skills

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):

    def __init__(self, name: str, skills=None) -> None:
        super().__init__(name, skills)
        front_skills = ["JavaScript", "HTML", "CSS"]
        self.skills.extend(front_skills)

    def create_awesome_web_page(self) -> str:
        message = f"{self.name} is creating a webpage..."
        page = "<h1>Hello world</h1>"
        print(message)
        return page


class BackendDeveloper(SoftwareEngineer):

    def __init__(self, name: str, skills=None) -> None:
        super().__init__(name, skills)
        back_skills = ["Python", "SQL", "Django"]
        self.skills.extend(back_skills)

    def create_powerful_api(self) -> str:
        message = f"{self.name} is creating an API..."
        api = "http://127.0.0.1:8000"
        print(message)
        return api


class AndroidDeveloper(SoftwareEngineer):

    def __init__(self, name: str, skills=None) -> None:
        super().__init__(name, skills)
        android_skills = ["Java", "Android studio"]
        self.skills.extend(android_skills)

    def create_smooth_mobile_app(self) -> str:
        message = f"{self.name} is creating a mobile app..."
        mobile = "Ads every three swipes"
        print(message)
        return mobile


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):

    def __init__(self, name: str, skills=None) -> None:
        super().__init__(name, skills)

    def create_web_application(self) -> None:
        message = f"{self.name} started creating a web application..."
        print(message)
        self.create_powerful_api()
        self.create_awesome_web_page()
