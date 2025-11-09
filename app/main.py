class SoftwareEngineer:
    def __init__(self, name):
        self.name = name
        self.skills = []

    def learn_skill(self, skill):
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name):
        super().__init__(name)
        self.skills.extend(["JavaScript", "HTML", "CSS"])

    def create_awesome_web_page(self):
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name):
        super().__init__(name)
        self.skills.extend(["Python", "SQL", "Django"])

    def create_powerful_api(self):
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name):
        super().__init__(name)
        self.skills.extend(["Java", "Android studio"])

    def create_smooth_mobile_app(self):
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    def __init__(self, name):
        super().__init__(name)
        for skill in ["JavaScript", "HTML", "CSS"]:
            if skill not in self.skills:
                self.skills.append(skill)

    def create_web_application(self):
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()

engineer = SoftwareEngineer("Max")
print(engineer.skills)          # []
engineer.learn_skill("Python")
print(engineer.skills)          # ["Python"]

front_dev = FrontendDeveloper("Alisa")
print(front_dev.skills)         # ["JavaScript", "HTML", "CSS"]
page = front_dev.create_awesome_web_page()
print(page)                     # "<h1>Hello world</h1>"

backend_dev = BackendDeveloper("Bob")
print(backend_dev.skills)       # ["Python", "SQL", "Django"]
address = backend_dev.create_powerful_api()
print(address)                  # "http://127.0.0.1:8000"

android_dev = AndroidDeveloper("Beth")
print(android_dev.skills)       # ["Java", "Android studio"]
app = android_dev.create_smooth_mobile_app()
print(app)                      # "Ads every three swipes"

full_stack_dev = FullStackDeveloper("Tom")
print(full_stack_dev.skills)
# ["Python", "SQL", "Django", "JavaScript", "HTML", "CSS"]
full_stack_dev.create_web_application()
# Tom started creating a web application...
# Tom is creating an API...
# Tom is creating a webpage...
