from .engineer import SoftwareEngineer, TSkills


# variables
default_fe_developer_skills: TSkills = ["JavaScript", "HTML", "CSS"]


# mixins
class FrontendMixin:
    @staticmethod
    def create_app_page() -> str:
        return "<h1>Hello world</h1>"


class FrontendDeveloper(SoftwareEngineer, FrontendMixin):
    def __init__(
            self,
            name: str,
    ) -> None:
        super().__init__(name)
        self.skills.extend(default_fe_developer_skills)

    def create_awesome_web_page(self) -> str:
        print(f"{self.name} is creating a webpage...")
        return self.create_app_page()
