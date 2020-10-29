# framework_adaptor

> Auto-generated documentation for [pytaintx.web_frameworks.framework_adaptor](../../../pytaintx/web_frameworks/framework_adaptor.py) module.

A generic framework adaptor that leaves route criteria to the caller.

- [Pytaintx](../../README.md#pytaintx-index) / [Modules](../../README.md#pytaintx-modules) / [pytaintx](../index.md#pytaintx) / [web_frameworks](index.md#web_frameworks) / framework_adaptor
    - [FrameworkAdaptor](#frameworkadaptor)
        - [FrameworkAdaptor().find_route_functions_taint_args](#frameworkadaptorfind_route_functions_taint_args)
        - [FrameworkAdaptor().get_func_cfg_with_tainted_args](#frameworkadaptorget_func_cfg_with_tainted_args)
        - [FrameworkAdaptor().run](#frameworkadaptorrun)

## FrameworkAdaptor

[[find in source code]](../../../pytaintx/web_frameworks/framework_adaptor.py#L17)

```python
class FrameworkAdaptor():
    def __init__(cfg_list, project_modules, local_modules, is_route_function):
```

An engine that uses the template pattern to find all
entry points in a framework and then taints their arguments.

### FrameworkAdaptor().find_route_functions_taint_args

[[find in source code]](../../../pytaintx/web_frameworks/framework_adaptor.py#L77)

```python
def find_route_functions_taint_args():
```

Find all route functions and taint all of their arguments.

#### Yields

CFG of each route function, with args marked as tainted.

### FrameworkAdaptor().get_func_cfg_with_tainted_args

[[find in source code]](../../../pytaintx/web_frameworks/framework_adaptor.py#L35)

```python
def get_func_cfg_with_tainted_args(definition):
```

Build a function cfg and return it, with all arguments tainted.

### FrameworkAdaptor().run

[[find in source code]](../../../pytaintx/web_frameworks/framework_adaptor.py#L87)

```python
def run():
```

Run find_route_functions_taint_args on each CFG.
