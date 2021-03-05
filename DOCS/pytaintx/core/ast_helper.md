# ast_helper

> Auto-generated documentation for [pytaintx.core.ast_helper](../../../pytaintx/core/ast_helper.py) module.

This module contains helper function.
Useful when working with the ast module.

- [Pytaintx](../../README.md#pytaintx-index) / [Modules](../../README.md#pytaintx-modules) / [pytaintx](../index.md#pytaintx) / [core](index.md#core) / ast_helper
    - [Arguments](#arguments)
    - [generate_ast](#generate_ast)
    - [get_call_names](#get_call_names)
    - [get_call_names_as_string](#get_call_names_as_string)

## Arguments

[[find in source code]](../../../pytaintx/core/ast_helper.py#L82)

```python
class Arguments():
    def __init__(args):
```

Represents arguments of a function.

## generate_ast

[[find in source code]](../../../pytaintx/core/ast_helper.py#L28)

```python
@lru_cache()
def generate_ast(path):
```

Generate an Abstract Syntax Tree using the ast module.

#### Arguments

- `path(str)` - The path to the file e.g. example/foo/bar.py

## get_call_names

[[find in source code]](../../../pytaintx/core/ast_helper.py#L67)

```python
def get_call_names(node):
```

Get a list of call names.

## get_call_names_as_string

[[find in source code]](../../../pytaintx/core/ast_helper.py#L77)

```python
def get_call_names_as_string(node):
```

Get a list of call names as a string.
