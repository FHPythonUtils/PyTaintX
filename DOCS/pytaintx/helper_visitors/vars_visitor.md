# vars_visitor

> Auto-generated documentation for [pytaintx.helper_visitors.vars_visitor](../../../pytaintx/helper_visitors/vars_visitor.py) module.

- [Pytaintx](../../README.md#pytaintx-index) / [Modules](../../README.md#pytaintx-modules) / [pytaintx](../index.md#pytaintx) / [helper_visitors](index.md#helper_visitors) / vars_visitor
    - [VarsVisitor](#varsvisitor)
        - [VarsVisitor().comprehension](#varsvisitorcomprehension)
        - [VarsVisitor().slicev](#varsvisitorslicev)
        - [VarsVisitor().visit_Attribute](#varsvisitorvisit_attribute)
        - [VarsVisitor().visit_BinOp](#varsvisitorvisit_binop)
        - [VarsVisitor().visit_BoolOp](#varsvisitorvisit_boolop)
        - [VarsVisitor().visit_Call](#varsvisitorvisit_call)
        - [VarsVisitor().visit_Compare](#varsvisitorvisit_compare)
        - [VarsVisitor().visit_Dict](#varsvisitorvisit_dict)
        - [VarsVisitor().visit_DictComp](#varsvisitorvisit_dictcomp)
        - [VarsVisitor().visit_GeneratorComp](#varsvisitorvisit_generatorcomp)
        - [VarsVisitor().visit_IfExp](#varsvisitorvisit_ifexp)
        - [VarsVisitor().visit_Lambda](#varsvisitorvisit_lambda)
        - [VarsVisitor().visit_List](#varsvisitorvisit_list)
        - [VarsVisitor().visit_ListComp](#varsvisitorvisit_listcomp)
        - [VarsVisitor().visit_Name](#varsvisitorvisit_name)
        - [VarsVisitor().visit_Set](#varsvisitorvisit_set)
        - [VarsVisitor().visit_SetComp](#varsvisitorvisit_setcomp)
        - [VarsVisitor().visit_Starred](#varsvisitorvisit_starred)
        - [VarsVisitor().visit_Subscript](#varsvisitorvisit_subscript)
        - [VarsVisitor().visit_Tuple](#varsvisitorvisit_tuple)
        - [VarsVisitor().visit_UnaryOp](#varsvisitorvisit_unaryop)
        - [VarsVisitor().visit_Yield](#varsvisitorvisit_yield)
        - [VarsVisitor().visit_YieldFrom](#varsvisitorvisit_yieldfrom)
        - [VarsVisitor().visit_curried_call_inside_call_args](#varsvisitorvisit_curried_call_inside_call_args)

## VarsVisitor

[[find in source code]](../../../pytaintx/helper_visitors/vars_visitor.py#L7)

```python
class VarsVisitor(ast.NodeVisitor):
    def __init__():
```

### VarsVisitor().comprehension

[[find in source code]](../../../pytaintx/helper_visitors/vars_visitor.py#L44)

```python
def comprehension(node):
```

### VarsVisitor().slicev

[[find in source code]](../../../pytaintx/helper_visitors/vars_visitor.py#L131)

```python
def slicev(node):
```

### VarsVisitor().visit_Attribute

[[find in source code]](../../../pytaintx/helper_visitors/vars_visitor.py#L125)

```python
def visit_Attribute(node):
```

### VarsVisitor().visit_BinOp

[[find in source code]](../../../pytaintx/helper_visitors/vars_visitor.py#L18)

```python
def visit_BinOp(node):
```

### VarsVisitor().visit_BoolOp

[[find in source code]](../../../pytaintx/helper_visitors/vars_visitor.py#L14)

```python
def visit_BoolOp(node):
```

### VarsVisitor().visit_Call

[[find in source code]](../../../pytaintx/helper_visitors/vars_visitor.py#L83)

```python
def visit_Call(node):
```

### VarsVisitor().visit_Compare

[[find in source code]](../../../pytaintx/helper_visitors/vars_visitor.py#L78)

```python
def visit_Compare(node):
```

### VarsVisitor().visit_Dict

[[find in source code]](../../../pytaintx/helper_visitors/vars_visitor.py#L33)

```python
def visit_Dict(node):
```

### VarsVisitor().visit_DictComp

[[find in source code]](../../../pytaintx/helper_visitors/vars_visitor.py#L60)

```python
def visit_DictComp(node):
```

### VarsVisitor().visit_GeneratorComp

[[find in source code]](../../../pytaintx/helper_visitors/vars_visitor.py#L66)

```python
def visit_GeneratorComp(node):
```

### VarsVisitor().visit_IfExp

[[find in source code]](../../../pytaintx/helper_visitors/vars_visitor.py#L28)

```python
def visit_IfExp(node):
```

### VarsVisitor().visit_Lambda

[[find in source code]](../../../pytaintx/helper_visitors/vars_visitor.py#L25)

```python
def visit_Lambda(node):
```

### VarsVisitor().visit_List

[[find in source code]](../../../pytaintx/helper_visitors/vars_visitor.py#L156)

```python
def visit_List(node):
```

### VarsVisitor().visit_ListComp

[[find in source code]](../../../pytaintx/helper_visitors/vars_visitor.py#L50)

```python
def visit_ListComp(node):
```

### VarsVisitor().visit_Name

[[find in source code]](../../../pytaintx/helper_visitors/vars_visitor.py#L11)

```python
def visit_Name(node):
```

### VarsVisitor().visit_Set

[[find in source code]](../../../pytaintx/helper_visitors/vars_visitor.py#L40)

```python
def visit_Set(node):
```

### VarsVisitor().visit_SetComp

[[find in source code]](../../../pytaintx/helper_visitors/vars_visitor.py#L55)

```python
def visit_SetComp(node):
```

### VarsVisitor().visit_Starred

[[find in source code]](../../../pytaintx/helper_visitors/vars_visitor.py#L153)

```python
def visit_Starred(node):
```

### VarsVisitor().visit_Subscript

[[find in source code]](../../../pytaintx/helper_visitors/vars_visitor.py#L146)

```python
def visit_Subscript(node):
```

### VarsVisitor().visit_Tuple

[[find in source code]](../../../pytaintx/helper_visitors/vars_visitor.py#L160)

```python
def visit_Tuple(node):
```

### VarsVisitor().visit_UnaryOp

[[find in source code]](../../../pytaintx/helper_visitors/vars_visitor.py#L22)

```python
def visit_UnaryOp(node):
```

### VarsVisitor().visit_Yield

[[find in source code]](../../../pytaintx/helper_visitors/vars_visitor.py#L71)

```python
def visit_Yield(node):
```

### VarsVisitor().visit_YieldFrom

[[find in source code]](../../../pytaintx/helper_visitors/vars_visitor.py#L75)

```python
def visit_YieldFrom(node):
```

### VarsVisitor().visit_curried_call_inside_call_args

[[find in source code]](../../../pytaintx/helper_visitors/vars_visitor.py#L106)

```python
def visit_curried_call_inside_call_args(inner_call):
```
