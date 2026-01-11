# app/main.py

class SoftwareEngineer:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.skills: list[str] = []

    def learn_skill(self, skill: str) -> None:
        """Додати навичку до списку"""
        self.skills.append(skill)

    def create_awesome_web_page(self) -> str:
        """Створення веб-сторінки"""
        print(f"{self.name} is creating a webpage...")
        self.skills.extend(["JavaScript", "HTML", "CSS"])
        return "<h1>Hello world</h1>"

    def create_powerful_api(self) -> str:
        """Створення API"""
        print(f"{self.name} is creating an API...")
        self.skills.extend(["Python", "SQL", "Django"])
        return "http://127.0.0.1:8000"

    def create_smooth_mobile_app(self) -> str:
        """Створення мобільного додатку"""
        print(f"{self.name} is creating a mobile app...")
        self.skills.extend(["Java", "Android Studio"])
        return "Ads every three swipes"

    def create_web_application(self) -> None:
        """Створення повноцінного веб-застосунку"""
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()


# -----------------------------
# Спеціалізовані класи
# -----------------------------

class FrontendDeveloper(SoftwareEngineer):
    """Фронтенд розробник з дефолтними навичками"""
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(["JavaScript", "CSS", "HTML"])


class BackendDeveloper(SoftwareEngineer):
    """Бекенд розробник з дефолтними навичками"""
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(["Python", "SQL", "Django"])


class AndroidDeveloper(SoftwareEngineer):
    """Розробник мобільних додатків Android"""
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.skills.extend(["Java", "Android studio"])

    def create_smooth_mobile_app(self) -> str:
        # Друк відповідає очікуванням тестів
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    """Фулстек розробник: комбінує Frontend + Backend"""
    def __init__(self, name: str) -> None:
        super().__init__(name)  # порядок батьків: Frontend, Backend
