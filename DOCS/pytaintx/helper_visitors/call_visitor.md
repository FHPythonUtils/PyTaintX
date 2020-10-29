# call_visitor

> Auto-generated documentation for [pytaintx.helper_visitors.call_visitor](../../../pytaintx/helper_visitors/call_visitor.py) module.

- [Pytaintx](../../README.md#pytaintx-index) / [Modules](../../README.md#pytaintx-modules) / [pytaintx](../index.md#pytaintx) / [helper_visitors](index.md#helper_visitors) / call_visitor
    - [CallVisitor](#callvisitor)
        - [CallVisitor.get_call_visit_results](#callvisitorget_call_visit_results)
        - [CallVisitor().visit_Call](#callvisitorvisit_call)
    - [CallVisitorResults](#callvisitorresults)
        - [CallVisitorResults().all_results](#callvisitorresultsall_results)

## CallVisitor

[[find in source code]](../../../pytaintx/helper_visitors/call_visitor.py#L27)

```python
class CallVisitor(ast.NodeVisitor):
    def __init__(trigger_str):
```

### CallVisitor.get_call_visit_results

[[find in source code]](../../../pytaintx/helper_visitors/call_visitor.py#L54)

```python
@classmethod
def get_call_visit_results(trigger_str, node):
```

### CallVisitor().visit_Call

[[find in source code]](../../../pytaintx/helper_visitors/call_visitor.py#L34)

```python
def visit_Call(call_node):
```

## CallVisitorResults

[[find in source code]](../../../pytaintx/helper_visitors/call_visitor.py#L10)

```python
class CallVisitorResults(
    namedtuple(
        'CallVisitorResults',
        ('args', 'kwargs', 'unknown_args', 'unknown_kwargs'),
    ),
):
```

### CallVisitorResults().all_results

[[find in source code]](../../../pytaintx/helper_visitors/call_visitor.py#L18)

```python
def all_results():
```
