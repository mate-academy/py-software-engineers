from app.software_engineers.backend_developer import BackendDeveloper
from app.software_engineers.frontend_developer import FrontendDeveloper


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    def create_web_application(self) -> str:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()