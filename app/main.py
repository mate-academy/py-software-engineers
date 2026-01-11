class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.skills: list[str] = []  # список навичок інженера

    def learn_skill(self, skill: str) -> None:
        """Додати навичку до списку"""
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(["JavaScript", "HTML", "CSS"])

    def create_awesome_web_page(self) -> str:
        """Створення веб-сторінки"""
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(["Python", "SQL", "Django"])

    def create_powerful_api(self) -> str:
        """Створення API"""
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(["Java", "Android studio"])

    def create_smooth_mobile_app(self) -> str:
        """Створення мобільного додатку"""
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        frontend_skills = ["JavaScript", "HTML", "CSS"]
        self.skills.extend(
            skill for skill in frontend_skills if skill not in self.skills)

    def create_web_application(self) -> None:
        """Створення повноцінного веб-застосунку"""
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
