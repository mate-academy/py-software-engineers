class SoftwareEngineer:
    def __init__(self, name: str):
        self.name = name
        self.skills = []

    def learn_skill(self, skill: str):
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name):
        super().__init__(name)
        frontend_skills = ["JavaScript", "HTML", "CSS"]
        for lang in frontend_skills:
            self.learn_skill(lang)

    def create_awesome_web_page(self):
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str):
        super().__init__(name)
        backend_skills = ["Python", "SQL", "Django"]
        for lang in backend_skills:
            self.learn_skill(lang)

    def create_powerful_api(self):
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name):
        super().__init__(name)
        android_dev_skills = ["Java", "Android studio"]
        for lang in android_dev_skills:
            self.learn_skill(lang)

    def create_smooth_mobile_app(self):
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    def create_web_application(self):
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
