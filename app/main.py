class SoftwareEngineer:
    def __init__(self, name: str, *args) -> None:
        self.name = name
        self.skills = []
        if args:
            list_args = list(set(args))
            list_args.sort()
            self.skills.extend(list_args)

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str, *args) -> None:
        self.frontend_default_skills = ["CSS", "HTML", "JavaScript"]
        skills_for_init = self.frontend_default_skills + list(args)
        super().__init__(name, *skills_for_init)

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str, *args) -> None:
        self.backend_default_skills = ["Django", "Python", "SQL"]
        skills_for_init = self.backend_default_skills + list(args)
        super().__init__(name, *skills_for_init)

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str, *args) -> None:
        self.android_default_skills = ["Android studio", "Java"]
        skills_for_init = self.android_default_skills + list(args)
        super().__init__(name, *skills_for_init)

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    def __init__(self, name: str, *args) -> None:
        super().__init__(name, *args)

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
