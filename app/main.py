class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.skills = []

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name):
        super().__init__(name=name)
        self.skills = ["JavaScript", "HTML", "CSS"]

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str):
        super().__init__(name=name)
        self.skills = ["Python", "SQL", "Django"]

    def create_powerful_api(self):
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str):
        super().__init__(name=name)
        self.skills = ["Java", "Android studio"]

    def create_smooth_mobile_app(self):
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    def __init__(self, name: str):
        super().__init__(name=name)



    def create_web_application(self):
        print(f"{self.name} started creating a web application...")


fs1 = FullStackDeveloper('Ivan')
print(fs1.skills)
# print(fs1.create_powerful_api())






# android_dev = AndroidDeveloper("Beth")
# # android_dev.skills == [
# #     "Java",
# #     "Android studio",
# # ]
# print(android_dev.skills)
#
#
# app = android_dev.create_smooth_mobile_app()  # "Beth is creating a mobile app..."
# # app == "Ads every three swipes"
# print(app)


# backend_dev = BackendDeveloper("Bob")
# print(backend_dev.skills)
# address = backend_dev.create_powerful_api()  # "Bob is creating an API..."
# # address == "http://127.0.0.1:8000"
# print(address)

# front_dev = FrontendDeveloper("Alisa")
# print(front_dev.skills)
# front_dev.learn_skill("Python")
# print(front_dev.skills)
#
# page = front_dev.create_awesome_web_page()  # "Alisa is creating a webpage..."
# # page == "<h1>Hello world</h1>"
# print(page)

# front_dev.skills == [
#     "JavaScript",
#     "HTML",
#     "CSS",
# ]



# engineer = SoftwareEngineer("Max")
# print(engineer.skills)
# # engineer.skills == []
# engineer.learn_skill("Python")
# # engineer.skills == ["Python"]
# print(engineer.skills)
