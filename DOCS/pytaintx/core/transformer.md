# transformer

> Auto-generated documentation for [pytaintx.core.transformer](../../../pytaintx/core/transformer.py) module.

- [Pytaintx](../../README.md#pytaintx-index) / [Modules](../../README.md#pytaintx-modules) / [pytaintx](../index.md#pytaintx) / [core](index.md#core) / transformer
    - [AsyncTransformer](#asynctransformer)
        - [AsyncTransformer().visit_AsyncFor](#asynctransformervisit_asyncfor)
        - [AsyncTransformer().visit_AsyncFunctionDef](#asynctransformervisit_asyncfunctiondef)
        - [AsyncTransformer().visit_AsyncWith](#asynctransformervisit_asyncwith)
        - [AsyncTransformer().visit_Await](#asynctransformervisit_await)
    - [ChainedFunctionTransformer](#chainedfunctiontransformer)
        - [ChainedFunctionTransformer().visit_Assign](#chainedfunctiontransformervisit_assign)
        - [ChainedFunctionTransformer().visit_Return](#chainedfunctiontransformervisit_return)
        - [ChainedFunctionTransformer().visit_chain](#chainedfunctiontransformervisit_chain)
    - [IfExpRewriter](#ifexprewriter)
        - [IfExpRewriter().visit_FunctionDef](#ifexprewritervisit_functiondef)
        - [IfExpRewriter().visit_IfExp](#ifexprewritervisit_ifexp)
    - [IfExpTransformer](#ifexptransformer)
        - [IfExpTransformer().visit_FunctionDef](#ifexptransformervisit_functiondef)
        - [IfExpTransformer().visit_Module](#ifexptransformervisit_module)
        - [IfExpTransformer().visit_body](#ifexptransformervisit_body)
    - [PytTransformer](#pyttransformer)

## AsyncTransformer

[[find in source code]](../../../pytaintx/core/transformer.py#L4)

```python
class AsyncTransformer():
```

Converts all async nodes into their synchronous counterparts.

### AsyncTransformer().visit_AsyncFor

[[find in source code]](../../../pytaintx/core/transformer.py#L14)

```python
def visit_AsyncFor(node):
```

### AsyncTransformer().visit_AsyncFunctionDef

[[find in source code]](../../../pytaintx/core/transformer.py#L11)

```python
def visit_AsyncFunctionDef(node):
```

### AsyncTransformer().visit_AsyncWith

[[find in source code]](../../../pytaintx/core/transformer.py#L17)

```python
def visit_AsyncWith(node):
```

### AsyncTransformer().visit_Await

[[find in source code]](../../../pytaintx/core/transformer.py#L7)

```python
def visit_Await(node):
```

Awaits are treated as if the keyword was absent.

## ChainedFunctionTransformer

[[find in source code]](../../../pytaintx/core/transformer.py#L21)

```python
class ChainedFunctionTransformer():
```

### ChainedFunctionTransformer().visit_Assign

[[find in source code]](../../../pytaintx/core/transformer.py#L60)

```python
def visit_Assign(node):
```

### ChainedFunctionTransformer().visit_Return

[[find in source code]](../../../pytaintx/core/transformer.py#L63)

```python
def visit_Return(node):
```

### ChainedFunctionTransformer().visit_chain

[[find in source code]](../../../pytaintx/core/transformer.py#L22)

```python
def visit_chain(node, depth=1):
```

## IfExpRewriter

[[find in source code]](../../../pytaintx/core/transformer.py#L67)

```python
class IfExpRewriter(ast.NodeTransformer):
    def __init__(starting_index=0):
```

Splits IfExp ternary expressions containing complex tests into multiple statements

Will change

a if b(c) else d

into

a if __if_exp_0 else d

with Assign nodes in assignments [__if_exp_0 = b(c)]

### IfExpRewriter().visit_FunctionDef

[[find in source code]](../../../pytaintx/core/transformer.py#L106)

```python
def visit_FunctionDef(node):
```

### IfExpRewriter().visit_IfExp

[[find in source code]](../../../pytaintx/core/transformer.py#L86)

```python
def visit_IfExp(node):
```

## IfExpTransformer

[[find in source code]](../../../pytaintx/core/transformer.py#L110)

```python
class IfExpTransformer():
```

Goes through module and function bodies, adding extra Assign nodes due to IfExp expressions.

### IfExpTransformer().visit_FunctionDef

[[find in source code]](../../../pytaintx/core/transformer.py#L125)

```python
def visit_FunctionDef(node):
```

### IfExpTransformer().visit_Module

[[find in source code]](../../../pytaintx/core/transformer.py#L136)

```python
def visit_Module(node):
```

### IfExpTransformer().visit_body

[[find in source code]](../../../pytaintx/core/transformer.py#L113)

```python
def visit_body(nodes):
```

## PytTransformer

[[find in source code]](../../../pytaintx/core/transformer.py#L142)

```python
class PytTransformer(
    AsyncTransformer,
    IfExpTransformer,
    ChainedFunctionTransformer,
    ast.NodeTransformer,
):
```

#### See also

- [AsyncTransformer](#asynctransformer)
- [ChainedFunctionTransformer](#chainedfunctiontransformer)
- [IfExpTransformer](#ifexptransformer)
