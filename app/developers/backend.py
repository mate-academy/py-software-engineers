from .engineer import SoftwareEngineer, TSkills


# variables
default_be_developer_skills: TSkills = ["Python", "SQL", "Django"]


# mixins
class BackendMixin:
    @staticmethod
    def create_api() -> str:
        return "http://127.0.0.1:8000"


class BackendDeveloper(SoftwareEngineer, BackendMixin):
    def __init__(
            self,
            name: str,
    ) -> None:
        super().__init__(name)
        self.skills.extend(default_be_developer_skills)

    def create_powerful_api(self) -> str:
        print(f"{self.name} is creating an API...")
        return self.create_api()
