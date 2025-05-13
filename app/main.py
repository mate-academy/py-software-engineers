class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.skills = list()

    def learn_skill(self, *skill: str) -> None:
        for skill_ in skill:
            self.skills.append(skill_)

    def perform_task(self, task: str) -> None:
        print(f"{self.name} is creating {task}...")


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.learn_skill("JavaScript", "HTML", "CSS")

    def create_awesome_web_page(self) -> str:
        self.perform_task("a webpage")

        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.learn_skill("Python", "SQL", "Django")

    def create_powerful_api(self) -> str:
        self.perform_task("an API")

        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.learn_skill("Java", "Android studio")

    def create_smooth_mobile_app(self) -> str:
        self.perform_task("a mobile app")

        return "Ads every three swipes"


class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
