from __future__ import annotations

if __name__ == "__main__":
    from developers import SoftwareEngineer, FrontendDeveloper, \
        BackendDeveloper, AndroidDeveloper, FullStackDeveloper
else:
    from .developers import SoftwareEngineer, FrontendDeveloper, \
        BackendDeveloper, AndroidDeveloper, FullStackDeveloper


# Code test block
if __name__ == "__main__":
    # Test
    SoftwareEngineer("Max")
    FrontendDeveloper("Alisa")
    BackendDeveloper("Bob")
    AndroidDeveloper("Beth")

    full_stack_dev = FullStackDeveloper("Tom")
    full_stack_dev.create_web_application()
