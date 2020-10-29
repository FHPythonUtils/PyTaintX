# models

> Auto-generated documentation for [examples.django.taskManager.models](../../../../examples/django.nV/taskManager/models.py) module.

- [Pytaintx](../../../README.md#pytaintx-index) / [Modules](../../../README.md#pytaintx-modules) / `examples` / `django` / [taskManager](index.md#taskmanager) / models
    - [File](#file)
    - [Notes](#notes)
    - [Project](#project)
        - [Project().is_overdue](#projectis_overdue)
        - [Project().percent_complete](#projectpercent_complete)
        - [Project().was_created_recently](#projectwas_created_recently)
    - [Task](#task)
        - [Task().is_overdue](#taskis_overdue)
        - [Task().percent_complete](#taskpercent_complete)
        - [Task().was_created_recently](#taskwas_created_recently)
    - [UserProfile](#userprofile)

## File

[[find in source code]](../../../../examples/django.nV/taskManager/models.py#L99)

```python
class File(models.Model):
```

## Notes

[[find in source code]](../../../../examples/django.nV/taskManager/models.py#L88)

```python
class Notes(models.Model):
```

## Project

[[find in source code]](../../../../examples/django.nV/taskManager/models.py#L29)

```python
class Project(models.Model):
```

### Project().is_overdue

[[find in source code]](../../../../examples/django.nV/taskManager/models.py#L48)

```python
def is_overdue():
```

### Project().percent_complete

[[find in source code]](../../../../examples/django.nV/taskManager/models.py#L51)

```python
def percent_complete():
```

### Project().was_created_recently

[[find in source code]](../../../../examples/django.nV/taskManager/models.py#L45)

```python
def was_created_recently():
```

## Task

[[find in source code]](../../../../examples/django.nV/taskManager/models.py#L61)

```python
class Task(models.Model):
```

### Task().is_overdue

[[find in source code]](../../../../examples/django.nV/taskManager/models.py#L81)

```python
def is_overdue():
```

### Task().percent_complete

[[find in source code]](../../../../examples/django.nV/taskManager/models.py#L84)

```python
def percent_complete():
```

### Task().was_created_recently

[[find in source code]](../../../../examples/django.nV/taskManager/models.py#L78)

```python
def was_created_recently():
```

## UserProfile

[[find in source code]](../../../../examples/django.nV/taskManager/models.py#L23)

```python
class UserProfile(models.Model):
```
