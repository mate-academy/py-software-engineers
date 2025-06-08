class SoftwareEngineer:

    def __init__(self, name: str, skills: list[str] | None = None) -> None:
        self.name = name
        self.skills = skills.copy() if skills else []

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)
# class SoftwareEngineer:
#
# # Firstly, you should create `SoftwareEngineer` class,
# # which will be a parent for all other classes.
# # Its `__init__` method should take one parameter: `name` of the
# # engineer. Also, engineer should have `skills` attribute -
# # a list of his/her skills, such as `"Python"` or `"JavaScript"`.
# # skills should be initialized as an empty
# list and will be extended by the child classes.
#
#     def __init__(self, name: str, skills: list = []) -> None:
#         self.name = name
#         self.skills = skills
#
# # `SoftwareEngineer` class should have one method: `learn_skill` that
# # takes a `skill` of string type and should add it to the `skills` list.
#
#     def learn_skill(self, skill: str = []) -> None:
#         self.skills.extend(skill)


class FrontendDeveloper(SoftwareEngineer):

    def __init__(self, name: str, skills: list[str] | None = None) -> None:
        super().__init__(name, skills)
        self.skills.extend(["JavaScript", "HTML", "CSS"])

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"

# Write class `FrontendDeveloper`,
# # which should be a child of class `SoftwareEngineer`.
# # Its `__init__` method also takes the `name` of the engineer.
# # Instances of this class should
# extend the skills list with the following default skills:
# # `"JavaScript"`, `"HTML"`, `"CSS"`.
#
#
# class FrontendDeveloper(SoftwareEngineer):
#     def __init__(self, name: str,
#     skills: list = ["JavaScript", "HTML", "CSS"]) -> None:
#         super().__init__(name, skills)
#         self.skills.extend(skills)
# # It should have one additional method: `create_awesome_web_page`.
# # It should print a following string `"{name} is creating a webpage..."`
# # where `name` is the `name` of the engineer
# # and return the code of the created webpage: `"<h1>Hello world</h1>"`.
#
#     def create_awesome_web_page(self) -> str:
#         print(f"{self.name} is creating a webpage...")
#         return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str, skills: list[str] | None = None) -> None:
        super().__init__(name, skills)
        self.skills.extend(["Python", "SQL", "Django"])

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"

#
# # Write class `BackendDeveloper`,
# # which should be a child of class `SoftwareEngineer`.
# # Its `__init__` method also takes the `name` of the engineer.
# # Instances of this class should
# extend the skills list with the following default skills:
# # `"Python"`, `"SQL"`, `"Django"`.
#
#
# class BackendDeveloper(SoftwareEngineer):
#
#     def __init__(self, name: str,
#     skills: list = ["Python", "SQL", "Django"]) -> None:
#         super().__init__(name, skills)
#         self.skills.extend(skills)
#
# # It should have one additional method: `create_powerful_api`.
# # It should print a following string `"{name} is creating an API..."`
# # where `name` is the `name` of engineer
# and return address of the API: `"http://127.0.0.1:8000"`.
#
#     def create_powerful_api(self) -> str:
#         print(f"{self.name} is creating an API...")
#         return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str, skills: list[str] | None = None) -> None:
        super().__init__(name, skills)
        self.skills.extend(["Java", "Android studio"])

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"

#
# # Write class `AndroidDeveloper`,
# # which should be a child of class `SoftwareEngineer`.
# # Its `__init__` method also takes the `name` of the engineer.
# # Instances of this class should extend
# the skills list with the following default skills:
# # `"Java"`, `"Android studio"`.
#
# class AndroidDeveloper(SoftwareEngineer):
#
#     def __init__(self, name: str,
#     skills: list = ["Java", "Android studio"]) -> None:
#         super().__init__(name, skills)
#         self.skills.extend(skills)
#
# # It should have one additional method: `create_smooth_mobile_app`.
# # It should print a following string `"{name} is creating a mobile app..."`
# # where `name` is the `name` of engineer
# and return UX of the created app: `"Ads every three swipes"`.
#
#     def create_smooth_mobile_app(self) -> str:
#         print(f"{self.name} is creating a mobile app...")
#         return "Ads every three swipes"


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    def __init__(self, name: str, skills: list[str] | None = None) -> None:
        super().__init__(name, skills)

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()

# # Finally, create class `FullStackDeveloper`
# which should be a child of some already created classes.
# # It should have one additional method: `create_web_application`.
# # This method should print the following
# message: `"{name} started creating a web application..."`
# # and call `create_powerful_api`, `create_awesome_web_page` methods.
#
# class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
#
#     def __init__(self, name: str,
#     skills: list= ["Python", "SQL", "Django",
#     "JavaScript", "CSS", "HTML"]) -> None:
#         super().__init__(name, skills)
#         self.skills.extend(skills)
#
#     def create_web_application(self) -> None:
#         print(f"{self.name} started creating a web application...")
#         self.create_awesome_web_page()
#         self.create_awesome_web_page()
#
