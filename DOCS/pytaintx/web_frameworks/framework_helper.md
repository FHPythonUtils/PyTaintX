# framework_helper

> Auto-generated documentation for [pytaintx.web_frameworks.framework_helper](../../../pytaintx/web_frameworks/framework_helper.py) module.

Provides helper functions that help with determining if a function is a route function.

- [Pytaintx](../../README.md#pytaintx-index) / [Modules](../../README.md#pytaintx-modules) / [pytaintx](../index.md#pytaintx) / [web_frameworks](index.md#web_frameworks) / framework_helper
    - [is_django_view_function](#is_django_view_function)
    - [is_flask_route_function](#is_flask_route_function)
    - [is_function](#is_function)
    - [is\_function\_without\_leading\_](#is_function_without_leading_)

## is_django_view_function

[[find in source code]](../../../pytaintx/web_frameworks/framework_helper.py#L7)

```python
def is_django_view_function(ast_node):
```

## is_flask_route_function

[[find in source code]](../../../pytaintx/web_frameworks/framework_helper.py#L14)

```python
def is_flask_route_function(ast_node):
```

Check whether function uses a route decorator.

## is_function

[[find in source code]](../../../pytaintx/web_frameworks/framework_helper.py#L23)

```python
def is_function(function):
```

Always returns true because arg is always a function.

## is\_function\_without\_leading\_

[[find in source code]](../../../pytaintx/web_frameworks/framework_helper.py#L28)

```python
def is_function_without_leading_(ast_node):
```
