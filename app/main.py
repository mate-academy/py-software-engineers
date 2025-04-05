class SoftwareEngineer:
    def __init__(self, name):
        self.name = name
        self.skills = []

    def learn_skill(self, skill):
        self.skills.append(skill)

    def code(self):
        return "I'm coding..."


class FrontendDeveloper(SoftwareEngineer):
    def __init__(self, name):
        super().__init__(name)
        self.skills.extend(["JavaScript", "HTML", "CSS"])

    def create_ui(self):
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    def __init__(self, name):
        super().__init__(name)
        self.skills.extend(["Python", "SQL", "Django"])

    def create_api(self):
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    def __init__(self, name):
        super().__init__(name)
        self.skills.extend(["Java", "Android studio"])

    def build_android_app(self):
        return "Building .apk file..."
