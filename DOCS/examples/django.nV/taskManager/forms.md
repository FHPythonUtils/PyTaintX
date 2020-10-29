# forms

> Auto-generated documentation for [examples.django.taskManager.forms](../../../../examples/django.nV/taskManager/forms.py) module.

forms.py contains various Django forms for the application

- [Pytaintx](../../../README.md#pytaintx-index) / [Modules](../../../README.md#pytaintx-modules) / `examples` / `django` / [taskManager](index.md#taskmanager) / forms
    - [ProfileForm](#profileform)
    - [ProjectFileForm](#projectfileform)
    - [UserForm](#userform)
    - [get_my_choices_projects](#get_my_choices_projects)
    - [get_my_choices_tasks](#get_my_choices_tasks)
    - [get_my_choices_users](#get_my_choices_users)

## ProfileForm

[[find in source code]](../../../../examples/django.nV/taskManager/forms.py#L84)

```python
class ProfileForm(forms.Form):
```

Provides a form for editing your own profile

## ProjectFileForm

[[find in source code]](../../../../examples/django.nV/taskManager/forms.py#L78)

```python
class ProjectFileForm(forms.Form):
```

Used for uploading files attached to projects

## UserForm

[[find in source code]](../../../../examples/django.nV/taskManager/forms.py#L71)

```python
class UserForm(forms.ModelForm):
```

User registration form

## get_my_choices_projects

[[find in source code]](../../../../examples/django.nV/taskManager/forms.py#L55)

```python
def get_my_choices_projects():
```

 Retrieves all projects in the system
for the project management page

## get_my_choices_tasks

[[find in source code]](../../../../examples/django.nV/taskManager/forms.py#L36)

```python
def get_my_choices_tasks(current_proj):
```

 Retrieves all tasks in the system
for the task management page

## get_my_choices_users

[[find in source code]](../../../../examples/django.nV/taskManager/forms.py#L22)

```python
def get_my_choices_users():
```

 Retrieves a list of all users in the system
for the user management page
