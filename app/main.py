class SoftwareEngineer:
    def __init__(self, name):
        self.name = name
        self.skills = []

    def code(self):
        print(f"{self.name} is coding...")

    def learn_skills(self, *skills):
        self.skills.extend(skills)  # ✅ Uso de extend() ao invés de loop


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name):
        super().__init__(name)  # ✅ Chamada do __init__ da superclasse
        self.skills.extend(["JavaScript", "HTML", "CSS"])  # ✅ Skills padrão

    def create_awesome_web_page(self):
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name):
        super().__init__(name)
        self.skills.extend(["Python", "SQL", "Django"])

    def create_powerful_api(self):
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name):
        super().__init__(name)
        self.skills.extend(["Java", "Android studio"])

    def create_smooth_mobile_app(self):
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    def __init__(self, name):
        super().__init__(name)
        # O super() acima chama FrontendDeveloper.__init__, que já adiciona os skills de Frontend.
        # Precisamos adicionar manualmente os do Backend.
        self.skills.extend(["Python", "SQL", "Django"])

    def create_web_application(self):
        frontend = self.create_awesome_web_page()
        backend = self.create_powerful_api()
        return {
            "frontend": frontend,
            "backend": backend,
        }
