class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):
    # O __init__ foi removido porque era redundante. 
    # O Python chamará o dos pais automaticamente.

    def create_web_application(self):
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
