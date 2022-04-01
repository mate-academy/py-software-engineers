class SoftwareEngineer():

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


class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):

    def __init__(self, name):
        super().__init__(name)

    def create_web_application(self):
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()


if __name__ == "__main__":
    engineer = SoftwareEngineer("Max")
    print(engineer.skills)
    engineer.learn_skill("Python")
    print(engineer.skills)

    front_dev = FrontendDeveloper("Alisa")
    print(front_dev.skills)

    page = front_dev.create_awesome_web_page()
    # "Alise is creating a webpage..."
    print(page)

    backend_dev = BackendDeveloper("Bob")
    print(backend_dev.skills)
    address = backend_dev.create_powerful_api()
    # "Bob is creating an API..."
    print(address)

    android_dev = AndroidDeveloper("Beth")
    print(android_dev.skills)

    app = android_dev.create_smooth_mobile_app()
    # "Beth is creating a mobile app..."
    print(app)

    full_stack_dev = FullStackDeveloper("Tom")
    print(full_stack_dev.skills)

    full_stack_dev.create_web_application()
