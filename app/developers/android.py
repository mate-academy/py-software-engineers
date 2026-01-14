from .engineer import SoftwareEngineer, TSkills

# variables
default_android_developer_skills: TSkills = ["Java", "Android studio"]


class AndroidDeveloper(SoftwareEngineer):
    def __init__(
            self,
            name: str,
    ) -> None:
        super().__init__(name)
        self.skills.extend(default_android_developer_skills)

    def create_smooth_mobile_app(self) -> str:
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"
