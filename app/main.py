class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.skills = []

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)

class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(["JavaScript", "HTML", "CSS"])

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"

class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(["Python", "SQL", "Django"])

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"

class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(["Java", "Android studio"])

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"

class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()  # First create API
        self.create_awesome_web_page()  # Then create the webpage

class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight

class DeliveryDrone(FrontendDeveloper, BackendDeveloper):
    def __init__(self, name: str, weight: int, max_load_weight: int, current_load: Cargo = None, coords: list = None) -> None:
        super().__init__(name)
        self.weight = weight
        self.max_load_weight = max_load_weight
        self.current_load = current_load
        self.coords = coords or [0, 0, 0]

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
