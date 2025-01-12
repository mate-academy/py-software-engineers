class SoftwareEngineer:
    def __init__(self, name, skills):
        self.name = name
        self.skills = []

    def learn_skill(self, skill):
            self.skills.append(skill)

class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name):
        super().__init__(name)
        self.skills.extend(["JavaScript", "HTML", "CSS"])

    def create_awesome_web_page(self):
        print(f"{self.name} is creating webpage...")
        return "<h1>Hello world</h1>"

class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name):
        super().__init__(name)
        self.skills.extend(["Python", "SQL", "Django"])

    def create_powerful_api(self):
        print(f"{self.name}  is creating an API...")
        return "http://127.0.0.1:8000"

class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name):
        super().__init__(name)
        self.skills.extend(["Java", "Android studio"])

    def create_smooth_mobile_app(self):
        print(f"{self.name} is creating a mobile app...")
        return (f"Ads every three swipes")

class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    def __init__(self, name):
        super().__init__(name)
        self.skills = list(set(self.skills))


    def create_web_application(self):
        print(f"{self.name} started creating a web application...")
        ary = self.create_powerful_api()
        webpage = self.create_awesome_web_page()
        return ary, webpage


