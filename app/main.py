class SoftwareEngineer:
    def __init__(self, name):
        self.name = name
        self.skill = []


    def learn_skill(self, obj):
        self.skill.append(obj)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name):
        super().__init__(name)
        self.skill = []

    def expansion_skill(self, obj):
        self.skill.append("JavaScript", "HTML", "CSS")


    def create_awesome_web_page(self):
        print(f"{self.name} is creating a webpage")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name):
        super().__init__(name)
        self.skill = []

    def expansion_skill(self, obj):
        self.skill.append(obj)

    def create_powerful_api(self):
        print(f"{self.name} is creating an API")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name):
        super().__init__(name)
        self.skill = []

    def expansion_skill(self, obj):
        self.skill.append(obj)


    def create_smooth_mobile_app(self):
        print(f"{self.name} is creating a mobile app")
        return "Ads every three swipes"


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    def __init__(self, name):
        self.name = name
        super().__init__(name)


    def create_web_application(self):
        print(f"{self.name} started creating a web application")
        BackendDeveloper.create_powerful_api(self)
        FrontendDeveloper.create_awesome_web_page(self)









