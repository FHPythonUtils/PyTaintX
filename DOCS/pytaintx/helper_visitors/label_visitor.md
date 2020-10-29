# label_visitor

> Auto-generated documentation for [pytaintx.helper_visitors.label_visitor](../../../pytaintx/helper_visitors/label_visitor.py) module.

- [Pytaintx](../../README.md#pytaintx-index) / [Modules](../../README.md#pytaintx-modules) / [pytaintx](../index.md#pytaintx) / [helper_visitors](index.md#helper_visitors) / label_visitor
    - [LabelVisitor](#labelvisitor)
        - [LabelVisitor().comprehensions](#labelvisitorcomprehensions)
        - [LabelVisitor().handle_comma_separated](#labelvisitorhandle_comma_separated)
        - [LabelVisitor().insert_space](#labelvisitorinsert_space)
        - [LabelVisitor().slicev](#labelvisitorslicev)
        - [LabelVisitor().visit_Add](#labelvisitorvisit_add)
        - [LabelVisitor().visit_And](#labelvisitorvisit_and)
        - [LabelVisitor().visit_Assign](#labelvisitorvisit_assign)
        - [LabelVisitor().visit_Attribute](#labelvisitorvisit_attribute)
        - [LabelVisitor().visit_AugAssign](#labelvisitorvisit_augassign)
        - [LabelVisitor().visit_BinOp](#labelvisitorvisit_binop)
        - [LabelVisitor().visit_BitAnd](#labelvisitorvisit_bitand)
        - [LabelVisitor().visit_BitOr](#labelvisitorvisit_bitor)
        - [LabelVisitor().visit_BitXor](#labelvisitorvisit_bitxor)
        - [LabelVisitor().visit_BoolOp](#labelvisitorvisit_boolop)
        - [LabelVisitor().visit_Call](#labelvisitorvisit_call)
        - [LabelVisitor().visit_Compare](#labelvisitorvisit_compare)
        - [LabelVisitor().visit_DictComp](#labelvisitorvisit_dictcomp)
        - [LabelVisitor().visit_Div](#labelvisitorvisit_div)
        - [LabelVisitor().visit_Eq](#labelvisitorvisit_eq)
        - [LabelVisitor().visit_FloorDiv](#labelvisitorvisit_floordiv)
        - [LabelVisitor().visit_FormattedValue](#labelvisitorvisit_formattedvalue)
        - [LabelVisitor().visit_GeneratorExp](#labelvisitorvisit_generatorexp)
        - [LabelVisitor().visit_Gt](#labelvisitorvisit_gt)
        - [LabelVisitor().visit_GtE](#labelvisitorvisit_gte)
        - [LabelVisitor().visit_IfExp](#labelvisitorvisit_ifexp)
        - [LabelVisitor().visit_In](#labelvisitorvisit_in)
        - [LabelVisitor().visit_Invert](#labelvisitorvisit_invert)
        - [LabelVisitor().visit_Is](#labelvisitorvisit_is)
        - [LabelVisitor().visit_IsNot](#labelvisitorvisit_isnot)
        - [LabelVisitor().visit_JoinedStr](#labelvisitorvisit_joinedstr)
        - [LabelVisitor().visit_LShift](#labelvisitorvisit_lshift)
        - [LabelVisitor().visit_List](#labelvisitorvisit_list)
        - [LabelVisitor().visit_ListComp](#labelvisitorvisit_listcomp)
        - [LabelVisitor().visit_Lt](#labelvisitorvisit_lt)
        - [LabelVisitor().visit_LtE](#labelvisitorvisit_lte)
        - [LabelVisitor().visit_Mod](#labelvisitorvisit_mod)
        - [LabelVisitor().visit_Mult](#labelvisitorvisit_mult)
        - [LabelVisitor().visit_Name](#labelvisitorvisit_name)
        - [LabelVisitor().visit_NameConstant](#labelvisitorvisit_nameconstant)
        - [LabelVisitor().visit_Not](#labelvisitorvisit_not)
        - [LabelVisitor().visit_NotEq](#labelvisitorvisit_noteq)
        - [LabelVisitor().visit_NotIn](#labelvisitorvisit_notin)
        - [LabelVisitor().visit_Num](#labelvisitorvisit_num)
        - [LabelVisitor().visit_Or](#labelvisitorvisit_or)
        - [LabelVisitor().visit_Pow](#labelvisitorvisit_pow)
        - [LabelVisitor().visit_RShift](#labelvisitorvisit_rshift)
        - [LabelVisitor().visit_Raise](#labelvisitorvisit_raise)
        - [LabelVisitor().visit_Return](#labelvisitorvisit_return)
        - [LabelVisitor().visit_SetComp](#labelvisitorvisit_setcomp)
        - [LabelVisitor().visit_Starred](#labelvisitorvisit_starred)
        - [LabelVisitor().visit_Str](#labelvisitorvisit_str)
        - [LabelVisitor().visit_Sub](#labelvisitorvisit_sub)
        - [LabelVisitor().visit_Subscript](#labelvisitorvisit_subscript)
        - [LabelVisitor().visit_Tuple](#labelvisitorvisit_tuple)
        - [LabelVisitor().visit_UAdd](#labelvisitorvisit_uadd)
        - [LabelVisitor().visit_USub](#labelvisitorvisit_usub)
        - [LabelVisitor().visit_UnaryOp](#labelvisitorvisit_unaryop)
        - [LabelVisitor().visit_joined_str](#labelvisitorvisit_joined_str)
        - [LabelVisitor().visit_keyword](#labelvisitorvisit_keyword)
        - [LabelVisitor().visit_withitem](#labelvisitorvisit_withitem)
        - [LabelVisitor().vist_MatMult](#labelvisitorvist_matmult)

## LabelVisitor

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L4)

```python
class LabelVisitor(ast.NodeVisitor):
    def __init__():
```

### LabelVisitor().comprehensions

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L100)

```python
def comprehensions(node):
```

### LabelVisitor().handle_comma_separated

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L8)

```python
def handle_comma_separated(comma_separated_list):
```

### LabelVisitor().insert_space

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L162)

```python
def insert_space():
```

### LabelVisitor().slicev

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L177)

```python
def slicev(node):
```

### LabelVisitor().visit_Add

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L193)

```python
def visit_Add(node):
```

### LabelVisitor().visit_And

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L277)

```python
def visit_And(node):
```

### LabelVisitor().visit_Assign

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L50)

```python
def visit_Assign(node):
```

### LabelVisitor().visit_Attribute

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L139)

```python
def visit_Attribute(node):
```

### LabelVisitor().visit_AugAssign

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L58)

```python
def visit_AugAssign(node):
```

### LabelVisitor().visit_BinOp

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L79)

```python
def visit_BinOp(node):
```

### LabelVisitor().visit_BitAnd

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L226)

```python
def visit_BitAnd(node):
```

### LabelVisitor().visit_BitOr

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L220)

```python
def visit_BitOr(node):
```

### LabelVisitor().visit_BitXor

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L223)

```python
def visit_BitXor(node):
```

### LabelVisitor().visit_BoolOp

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L92)

```python
def visit_BoolOp(node):
```

### LabelVisitor().visit_Call

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L144)

```python
def visit_Call(node):
```

### LabelVisitor().visit_Compare

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L67)

```python
def visit_Compare(node):
```

### LabelVisitor().visit_DictComp

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L124)

```python
def visit_DictComp(node):
```

### LabelVisitor().visit_Div

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L205)

```python
def visit_Div(node):
```

### LabelVisitor().visit_Eq

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L233)

```python
def visit_Eq(node):
```

### LabelVisitor().visit_FloorDiv

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L229)

```python
def visit_FloorDiv(node):
```

### LabelVisitor().visit_FormattedValue

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L307)

```python
def visit_FormattedValue(node):
```

FormattedValue(expr value, int? conversion, expr? format_spec)

### LabelVisitor().visit_GeneratorExp

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L109)

```python
def visit_GeneratorExp(node):
```

### LabelVisitor().visit_Gt

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L236)

```python
def visit_Gt(node):
```

### LabelVisitor().visit_GtE

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L245)

```python
def visit_GtE(node):
```

### LabelVisitor().visit_IfExp

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L328)

```python
def visit_IfExp(node):
```

### LabelVisitor().visit_In

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L257)

```python
def visit_In(node):
```

### LabelVisitor().visit_Invert

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L264)

```python
def visit_Invert(node):
```

### LabelVisitor().visit_Is

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L251)

```python
def visit_Is(node):
```

### LabelVisitor().visit_IsNot

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L254)

```python
def visit_IsNot(node):
```

### LabelVisitor().visit_JoinedStr

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L299)

```python
def visit_JoinedStr(node):
```

JoinedStr(expr* values)

### LabelVisitor().visit_LShift

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L214)

```python
def visit_LShift(node):
```

### LabelVisitor().visit_List

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L23)

```python
def visit_List(node):
```

### LabelVisitor().visit_ListComp

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L114)

```python
def visit_ListComp(node):
```

### LabelVisitor().visit_Lt

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L239)

```python
def visit_Lt(node):
```

### LabelVisitor().visit_LtE

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L248)

```python
def visit_LtE(node):
```

### LabelVisitor().visit_Mod

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L208)

```python
def visit_Mod(node):
```

### LabelVisitor().visit_Mult

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L199)

```python
def visit_Mult(node):
```

### LabelVisitor().visit_Name

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L286)

```python
def visit_Name(node):
```

### LabelVisitor().visit_NameConstant

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L165)

```python
def visit_NameConstant(node):
```

### LabelVisitor().visit_Not

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L267)

```python
def visit_Not(node):
```

### LabelVisitor().visit_NotEq

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L242)

```python
def visit_NotEq(node):
```

### LabelVisitor().visit_NotIn

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L260)

```python
def visit_NotIn(node):
```

### LabelVisitor().visit_Num

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L283)

```python
def visit_Num(node):
```

### LabelVisitor().visit_Or

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L280)

```python
def visit_Or(node):
```

### LabelVisitor().visit_Pow

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L211)

```python
def visit_Pow(node):
```

### LabelVisitor().visit_RShift

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L217)

```python
def visit_RShift(node):
```

### LabelVisitor().visit_Raise

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L30)

```python
def visit_Raise(node):
```

### LabelVisitor().visit_Return

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L46)

```python
def visit_Return(node):
```

### LabelVisitor().visit_SetComp

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L119)

```python
def visit_SetComp(node):
```

### LabelVisitor().visit_Starred

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L324)

```python
def visit_Starred(node):
```

### LabelVisitor().visit_Str

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L289)

```python
def visit_Str(node):
```

### LabelVisitor().visit_Sub

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L196)

```python
def visit_Sub(node):
```

### LabelVisitor().visit_Subscript

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L168)

```python
def visit_Subscript(node):
```

### LabelVisitor().visit_Tuple

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L16)

```python
def visit_Tuple(node):
```

### LabelVisitor().visit_UAdd

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L270)

```python
def visit_UAdd(node):
```

### LabelVisitor().visit_USub

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L273)

```python
def visit_USub(node):
```

### LabelVisitor().visit_UnaryOp

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L88)

```python
def visit_UnaryOp(node):
```

### LabelVisitor().visit_joined_str

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L292)

```python
def visit_joined_str(node, surround=True):
```

### LabelVisitor().visit_keyword

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L156)

```python
def visit_keyword(node):
```

### LabelVisitor().visit_withitem

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L39)

```python
def visit_withitem(node):
```

### LabelVisitor().vist_MatMult

[[find in source code]](../../../pytaintx/helper_visitors/label_visitor.py#L202)

```python
def vist_MatMult(node):
```
