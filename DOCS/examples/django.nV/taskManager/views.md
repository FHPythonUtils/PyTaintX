# views

> Auto-generated documentation for [examples.django.taskManager.views](../../../../examples/django.nV/taskManager/views.py) module.

- [Pytaintx](../../../README.md#pytaintx-index) / [Modules](../../../README.md#pytaintx-modules) / `examples` / `django` / [taskManager](index.md#taskmanager) / views
    - [change_password](#change_password)
    - [dashboard](#dashboard)
    - [download](#download)
    - [download_profile_pic](#download_profile_pic)
    - [forgot_password](#forgot_password)
    - [index](#index)
    - [login](#login)
    - [logout_view](#logout_view)
    - [manage_groups](#manage_groups)
    - [manage_projects](#manage_projects)
    - [manage_tasks](#manage_tasks)
    - [note_create](#note_create)
    - [note_delete](#note_delete)
    - [note_edit](#note_edit)
    - [profile](#profile)
    - [profile_by_id](#profile_by_id)
    - [profile_view](#profile_view)
    - [project_create](#project_create)
    - [project_delete](#project_delete)
    - [project_details](#project_details)
    - [project_edit](#project_edit)
    - [project_list](#project_list)
    - [register](#register)
    - [reset_password](#reset_password)
    - [search](#search)
    - [show_tutorial](#show_tutorial)
    - [task_complete](#task_complete)
    - [task_create](#task_create)
    - [task_delete](#task_delete)
    - [task_details](#task_details)
    - [task_edit](#task_edit)
    - [task_list](#task_list)
    - [tm_settings](#tm_settings)
    - [tutorials](#tutorials)
    - [upload](#upload)

## change_password

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L806)

```python
@csrf_exempt
def change_password(request):
```

## dashboard

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L621)

```python
def dashboard(request):
```

## download

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L199)

```python
def download(request, file_id):
```

## download_profile_pic

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L213)

```python
def download_profile_pic(request, user_id):
```

## forgot_password

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L772)

```python
@csrf_exempt
def forgot_password(request):
```

## index

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L459)

```python
def index(request):
```

## login

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L383)

```python
def login(request):
```

## logout_view

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L378)

```python
def logout_view(request):
```

## manage_groups

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L112)

```python
def manage_groups(request):
```

## manage_projects

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L74)

```python
def manage_projects(request):
```

## manage_tasks

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L39)

```python
def manage_tasks(request, project_id):
```

## note_create

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L523)

```python
def note_create(request, project_id, task_id):
```

## note_delete

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L574)

```python
def note_delete(request, project_id, task_id, note_id):
```

## note_edit

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L547)

```python
def note_edit(request, project_id, task_id, note_id):
```

## profile

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L696)

```python
def profile(request):
```

## profile_by_id

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L703)

```python
@csrf_exempt
def profile_by_id(request, user_id):
```

## profile_view

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L484)

```python
def profile_view(request, user_id):
```

## project_create

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L315)

```python
def project_create(request):
```

## project_delete

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L369)

```python
def project_delete(request, project_id):
```

## project_details

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L504)

```python
def project_details(request, project_id):
```

## project_edit

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L343)

```python
def project_edit(request, project_id):
```

## project_list

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L633)

```python
def project_list(request):
```

## register

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L414)

```python
def register(request):
```

## reset_password

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L732)

```python
@csrf_exempt
def reset_password(request):
```

## search

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L654)

```python
def search(request):
```

## show_tutorial

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L677)

```python
def show_tutorial(request, vuln_id):
```

## task_complete

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L304)

```python
def task_complete(request, project_id, task_id):
```

## task_create

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L233)

```python
def task_create(request, project_id):
```

## task_delete

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L292)

```python
def task_delete(request, project_id, task_id):
```

## task_details

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L586)

```python
def task_details(request, project_id, task_id):
```

## task_edit

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L266)

```python
def task_edit(request, project_id, task_id):
```

## task_list

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L648)

```python
def task_list(request):
```

## tm_settings

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L830)

```python
def tm_settings(request):
```

## tutorials

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L671)

```python
def tutorials(request):
```

## upload

[[find in source code]](../../../../examples/django.nV/taskManager/views.py#L170)

```python
def upload(request, project_id):
```
