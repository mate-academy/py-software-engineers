from .engineer import TSkills
from .backend import BackendDeveloper, default_be_developer_skills
from .frontend import FrontendDeveloper, default_fe_developer_skills


# variables
default_fs_developer_skills: TSkills = [
    *default_fe_developer_skills,
    *default_be_developer_skills
]


class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    def __init__(
            self,
            name: str,
    ) -> None:
        super().__init__(name)
        self.skills = default_fs_developer_skills

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")

        self.create_powerful_api()
        self.create_awesome_web_page()
