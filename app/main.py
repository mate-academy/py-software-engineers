class SoftwareEngineer:

    def __init__(self, name, skills=None):
        self.name = name
        self.skills = [] if skills is None else skills

    def learn_skill(self, skill):
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name, skills=None):
        super().__init__(name, skills=skills)
        self.skills = [
            "JavaScript",
            "HTML",
            "CSS"
        ] if skills is None else skills

    def create_awesome_web_page(self):
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name, skills=None):
        super().__init__(name, skills=skills)
        self.skills = [
            "Python",
            "SQL",
            "Django"
        ] if skills is None else skills

    def create_powerful_api(self):
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name, skills=None):
        super().__init__(name, skills=skills)
        self.skills = [
            "Java",
            "Android studio"
        ] if skills is None else skills

    def create_smooth_mobile_app(self):
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    def __init__(self, name, skills=None):
        super().__init__(name, skills=skills)
        self.skills = [
            "Python",
            "SQL",
            "Django",
            "JavaScript",
            "HTML",
            "CSS"
        ]

    def create_web_application(self):
        print(f'{self.name} started creating a web application...')
        super().create_powerful_api()
        super().create_awesome_web_page()
jk,j