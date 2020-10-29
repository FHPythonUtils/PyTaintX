# right_hand_side_visitor

> Auto-generated documentation for [pytaintx.helper_visitors.right_hand_side_visitor](../../../pytaintx/helper_visitors/right_hand_side_visitor.py) module.

Contains a class that finds all names.
Used to find all variables on a right hand side(RHS) of assignment.

- [Pytaintx](../../README.md#pytaintx-index) / [Modules](../../README.md#pytaintx-modules) / [pytaintx](../index.md#pytaintx) / [helper_visitors](index.md#helper_visitors) / right_hand_side_visitor
    - [RHSVisitor](#rhsvisitor)
        - [RHSVisitor.result_for_node](#rhsvisitorresult_for_node)
        - [RHSVisitor().visit_Call](#rhsvisitorvisit_call)
        - [RHSVisitor().visit_IfExp](#rhsvisitorvisit_ifexp)
        - [RHSVisitor().visit_Name](#rhsvisitorvisit_name)

## RHSVisitor

[[find in source code]](../../../pytaintx/helper_visitors/right_hand_side_visitor.py#L7)

```python
class RHSVisitor(ast.NodeVisitor):
    def __init__():
```

Visitor collecting all names.

### RHSVisitor.result_for_node

[[find in source code]](../../../pytaintx/helper_visitors/right_hand_side_visitor.py#L30)

```python
@classmethod
def result_for_node(node):
```

### RHSVisitor().visit_Call

[[find in source code]](../../../pytaintx/helper_visitors/right_hand_side_visitor.py#L17)

```python
def visit_Call(node):
```

### RHSVisitor().visit_IfExp

[[find in source code]](../../../pytaintx/helper_visitors/right_hand_side_visitor.py#L25)

```python
def visit_IfExp(node):
```

### RHSVisitor().visit_Name

[[find in source code]](../../../pytaintx/helper_visitors/right_hand_side_visitor.py#L14)

```python
def visit_Name(node):
```
