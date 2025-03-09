from app.developers.backend import BackendDeveloper
from app.developers.frontend import FrontendDeveloper
from app.developers.fullstack import FullStackDeveloper
from app.developers.android import AndroidDeveloper
from app.developers.engineer import SoftwareEngineer

print(BackendDeveloper.__mro__)
print(FrontendDeveloper.__mro__)
print(FullStackDeveloper.__mro__)
print(BackendDeveloper.__mro__)
print(AndroidDeveloper.__mro__)
print(SoftwareEngineer.__mro__)
