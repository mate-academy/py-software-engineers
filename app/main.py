from typing import List


class SoftwareEngineer:
    """Representa um engenheiro de software genérico."""

    def __init__(self, name: str) -> None:
        """Inicializa o engenheiro com um nome e uma lista de habilidades."""
        self.name = name
        self.skills: List[str] = []

    def learn_skill(self, skill: str) -> None:
        """Adiciona uma nova habilidade à lista de skills do engenheiro."""
        self.skills.append(skill)


class FrontendDeveloper(SoftwareEngineer):
    """Representa um desenvolvedor de frontend."""

    def __init__(self, name: str) -> None:
        """Inicializa o dev de frontend e adiciona habilidades padrão."""
        super().__init__(name)
        # AJUSTE: A ordem das habilidades foi corrigida p corresponder tarefa.
        self.skills.extend(["JavaScript", "HTML", "CSS"])

    def create_awesome_web_page(self) -> str:
        """Cria uma página da web e imprime uma mensagem de status."""
        print(f"{self.name} is creating a webpage...")
        return "<h1>Hello world</h1>"


class BackendDeveloper(SoftwareEngineer):
    """Representa um desenvolvedor de backend."""

    def __init__(self, name: str) -> None:
        """Inicializa o dev de backend e adiciona habilidades padrão."""
        super().__init__(name)
        # AJUSTE: A ordem das habilidades foi corrigida p corresponder tarefa.
        self.skills.extend(["Python", "SQL", "Django"])

    def create_powerful_api(self) -> str:
        """Cria uma API e imprime uma mensagem de status."""
        print(f"{self.name} is creating an API...")
        return "http://127.0.0.1:8000"


class AndroidDeveloper(SoftwareEngineer):
    """Representa um desenvolvedor Android."""

    def __init__(self, name: str) -> None:
        """Inicializa o desenvolvedor Android e adiciona habilidades padrão."""
        super().__init__(name)
        self.skills.extend(["Java", "Android studio"])

    def create_smooth_mobile_app(self) -> str:
        """Cria um aplicativo móvel e imprime uma mensagem de status."""
        print(f"{self.name} is creating a mobile app...")
        return "Ads every three swipes"


class FullStackDeveloper(FrontendDeveloper, BackendDeveloper):
    """Representa um desenvolvedor full-stack."""

    def create_web_application(self) -> None:
        """Cria aplicação web completa chamando os métodos de API e webpage."""
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()


# Bloco de execução para testar todas as classes
if __name__ == "__main__":
    engineer = SoftwareEngineer("Max")
    engineer.learn_skill("Python")
    print(f"Skills de {engineer.name}: {engineer.skills}")
    print("-" * 20)

    front_dev = FrontendDeveloper("Alisa")
    print(f"Skills de {front_dev.name}: {front_dev.skills}")
    page = front_dev.create_awesome_web_page()
    print(f"Página criada: {page}")
    print("-" * 20)

    backend_dev = BackendDeveloper("Bob")
    print(f"Skills de {backend_dev.name}: {backend_dev.skills}")
    address = backend_dev.create_powerful_api()
    print(f"Endereço da API: {address}")
    print("-" * 20)

    android_dev = AndroidDeveloper("Beth")
    print(f"Skills de {android_dev.name}: {android_dev.skills}")
    app_ux = android_dev.create_smooth_mobile_app()
    print(f"UX do App: {app_ux}")
    print("-" * 20)

    full_stack_dev = FullStackDeveloper("Tom")
    print(f"Skills de {full_stack_dev.name}: {full_stack_dev.skills}")
    full_stack_dev.create_web_application()
