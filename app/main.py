class SoftwareEngineer:
    skills = []

    def __init__(self, name: str):
        self.name = name

    def learn_skill(self, *args):
        for argument in args:
            self.skills.append(argument)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name):
        super().__init__(name)
        self.learn_skill("Javascript", "HTML", "CSS")

    def create_awesome_web_page(self):
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str):
        super().__init__(name)
        self.learn_skill("Python", "SQL", "Django")

    def create_powerful_api(self):
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str):
        super().__init__(name)
        self.learn_skill("Java", "Android studio")

    def create_smooth_mobile_app(self):
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    def __init__(self, name: str):
        super().__init__(name)

        self.skills = set(self.skills)
        self.skills = list(self.skills)

    def create_web_application(self):
        print(f"{self.name} started creating a web application...")

        self.create_powerful_api()
        self.create_awesome_web_page()

front_dev = FrontendDeveloper("Alisa")
print(front_dev.skills)

full_stack_dev = FullStackDeveloper("Tom")
print(full_stack_dev.skills)
full_stack_dev.create_web_application()
