# project_handler

> Auto-generated documentation for [pytaintx.core.project_handler](../../../pytaintx/core/project_handler.py) module.

Generates a list of CFGs from a path.

- [Pytaintx](../../README.md#pytaintx-index) / [Modules](../../README.md#pytaintx-modules) / [pytaintx](../index.md#pytaintx) / [core](index.md#core) / project_handler
    - [get_directory_modules](#get_directory_modules)
    - [get_modules](#get_modules)

The module finds all python modules and generates an ast for them.

## get_directory_modules

[[find in source code]](../../../pytaintx/core/project_handler.py#L11)

```python
def get_directory_modules(directory):
```

Return a list containing tuples of
e.g. ('__init__', 'example/import_test_project/__init__.py')

## get_modules

[[find in source code]](../../../pytaintx/core/project_handler.py#L34)

```python
def get_modules(path, prepend_module_root=True):
```

Return a list containing tuples of
e.g. ('test_project.utils', 'example/test_project/utils.py')
