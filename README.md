# Py Software Engineers

**Please note:** read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md)
before starting.

Firstly, you should create `SoftwareEngineer` class, 
which will be a parent for all other classes. 
Its `__init__` method should take one parameter: `name` of the 
engineer. Also, engineer should have `skills` attribute - 
a list of his/her skills, such as `"Python"` or `"JavaScript"`.
skills should be initialized as an empty list and will be extended by the child classes.

`SoftwareEngineer` class should have one method: `learn_skill` that 
takes a `skill` of string type and should add it to the `skills` list.

```python
engineer = SoftwareEngineer("Max")
# engineer.skills == [] 
engineer.learn_skill("Python")
# engineer.skills == ["Python"] 
```

Write class `FrontendDeveloper`, 
which should be a child of class `SoftwareEngineer`. 
Its `__init__` method also takes the `name` of the engineer. 
Instances of this class should extend the skills list with the following default skills:
`"JavaScript"`, `"HTML"`, `"CSS"`.

```python
front_dev = FrontendDeveloper("Alisa")
# front_dev.skills == [
#     "JavaScript",
#     "HTML",
#     "CSS",
# ]
```

It should have one additional method: `create_awesome_web_page`.
It should print a following string `"{name} is creating a webpage..."`
where `name` is the `name` of the engineer 
and return the code of the created webpage: `"<h1>Hello world</h1>"`.

```python
page = front_dev.create_awesome_web_page()  # "Alisa is creating a webpage..."
# page == "<h1>Hello world</h1>"
```

Write class `BackendDeveloper`, 
which should be a child of class `SoftwareEngineer`. 
Its `__init__` method also takes the `name` of the engineer. 
Instances of this class should extend the skills list with the following default skills:
`"Python"`, `"SQL"`, `"Django"`.

```python
backend_dev = BackendDeveloper("Bob")
# backend_dev.skills == [
#     "Python",
#     "SQL",
#     "Django",
# ]
```

It should have one additional method: `create_powerful_api`.
It should print a following string `"{name} is creating an API..."`
where `name` is the `name` of engineer and return address of the API: `"http://127.0.0.1:8000"`.

```python
address = backend_dev.create_powerful_api()  # "Bob is creating an API..."
# address == "http://127.0.0.1:8000"
```

Write class `AndroidDeveloper`, 
which should be a child of class `SoftwareEngineer`. 
Its `__init__` method also takes the `name` of the engineer. 
Instances of this class should extend the skills list with the following default skills:
`"Java"`, `"Android studio"`.

```python
android_dev = AndroidDeveloper("Beth")
# android_dev.skills == [
#     "Java", 
#     "Android studio",
# ]
```

It should have one additional method: `create_smooth_mobile_app`.
It should print a following string `"{name} is creating a mobile app..."`
where `name` is the `name` of engineer and return UX of the created app: `"Ads every three swipes"`.

```python
app = android_dev.create_smooth_mobile_app()  # "Beth is creating a mobile app..."
# app == "Ads every three swipes"
```

Finally, create class `FullStackDeveloper` which should be a child of some already created classes.
It should have one additional method: `create_web_application`.
This method should print the following message: `"{name} started creating a web application..."`
and call `create_powerful_api`, `create_awesome_web_page` methods.

```python
full_stack_dev = FullStackDeveloper("Tom")
# full_stack_dev.skills == [
#     "Python",
#     "SQL",
#     "Django",
#     "JavaScript",
#     "HTML",
#     "CSS",
# ]

full_stack_dev.create_web_application()
# Tom started creating a web application...
# Tom is creating an API...
# Tom is creating a webpage...
```

### Note: Check your code using this [checklist](checklist.md) before pushing your solution.
