from app.developers.backend_developer import BackendDeveloper


class FullStackDeveloper(BackendDeveloper):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend([
            "JavaScript",
            "CSS",
            "HTML",
        ])

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"

    def create_web_application(self) -> None:
        print(
            f"{self.name} started creating a web application..."
        )
        self.create_powerful_api()
        self.create_awesome_web_page()
