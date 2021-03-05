# stmt_visitor

> Auto-generated documentation for [pytaintx.cfg.stmt_visitor](../../../pytaintx/cfg/stmt_visitor.py) module.

- [Pytaintx](../../README.md#pytaintx-index) / [Modules](../../README.md#pytaintx-modules) / [pytaintx](../index.md#pytaintx) / [cfg](index.md#cfg) / stmt_visitor
    - [StmtVisitor](#stmtvisitor)
        - [StmtVisitor().add_blackbox_or_builtin_call](#stmtvisitoradd_blackbox_or_builtin_call)
        - [StmtVisitor().add_module](#stmtvisitoradd_module)
        - [StmtVisitor().add_to_definitions](#stmtvisitoradd_to_definitions)
        - [StmtVisitor().append_node](#stmtvisitorappend_node)
        - [StmtVisitor().assign_multi_target](#stmtvisitorassign_multi_target)
        - [StmtVisitor().assign_tuple_target](#stmtvisitorassign_tuple_target)
        - [StmtVisitor().assignment_call_node](#stmtvisitorassignment_call_node)
        - [StmtVisitor().from_directory_import](#stmtvisitorfrom_directory_import)
        - [StmtVisitor().get_parent_definitions](#stmtvisitorget_parent_definitions)
        - [StmtVisitor().handle_or_else](#stmtvisitorhandle_or_else)
        - [StmtVisitor().handle_relative_import](#stmtvisitorhandle_relative_import)
        - [StmtVisitor().handle_stmt_star_ignore_node](#stmtvisitorhandle_stmt_star_ignore_node)
        - [StmtVisitor().import_package](#stmtvisitorimport_package)
        - [StmtVisitor().loop_node_skeleton](#stmtvisitorloop_node_skeleton)
        - [StmtVisitor().process_loop_funcs](#stmtvisitorprocess_loop_funcs)
        - [StmtVisitor().stmt_star_handler](#stmtvisitorstmt_star_handler)
        - [StmtVisitor().visit_AnnAssign](#stmtvisitorvisit_annassign)
        - [StmtVisitor().visit_Assert](#stmtvisitorvisit_assert)
        - [StmtVisitor().visit_Assign](#stmtvisitorvisit_assign)
        - [StmtVisitor().visit_AugAssign](#stmtvisitorvisit_augassign)
        - [StmtVisitor().visit_Break](#stmtvisitorvisit_break)
        - [StmtVisitor().visit_ClassDef](#stmtvisitorvisit_classdef)
        - [StmtVisitor().visit_Continue](#stmtvisitorvisit_continue)
        - [StmtVisitor().visit_Delete](#stmtvisitorvisit_delete)
        - [StmtVisitor().visit_Expr](#stmtvisitorvisit_expr)
        - [StmtVisitor().visit_For](#stmtvisitorvisit_for)
        - [StmtVisitor().visit_FunctionDef](#stmtvisitorvisit_functiondef)
        - [StmtVisitor().visit_Global](#stmtvisitorvisit_global)
        - [StmtVisitor().visit_If](#stmtvisitorvisit_if)
        - [StmtVisitor().visit_Import](#stmtvisitorvisit_import)
        - [StmtVisitor().visit_ImportFrom](#stmtvisitorvisit_importfrom)
        - [StmtVisitor().visit_Module](#stmtvisitorvisit_module)
        - [StmtVisitor().visit_Pass](#stmtvisitorvisit_pass)
        - [StmtVisitor().visit_Raise](#stmtvisitorvisit_raise)
        - [StmtVisitor().visit_Return](#stmtvisitorvisit_return)
        - [StmtVisitor().visit_Try](#stmtvisitorvisit_try)
        - [StmtVisitor().visit_While](#stmtvisitorvisit_while)
        - [StmtVisitor().visit_With](#stmtvisitorvisit_with)
        - [StmtVisitor().visit_miscelleaneous_node](#stmtvisitorvisit_miscelleaneous_node)

## StmtVisitor

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L47)

```python
class StmtVisitor(ast.NodeVisitor):
    def __init__(allow_local_directory_imports=True):
```

### StmtVisitor().add_blackbox_or_builtin_call

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L548)

```python
def add_blackbox_or_builtin_call(node, blackbox):
```

Processes a blackbox or builtin function when it is called.
Nothing gets assigned to ret_func_foo in the builtin/blackbox case.

Increments self.function_call_index each time it is called, we can refer to it as N in the comments.
Create e.g. ~call_1 = ret_func_foo RestoreNode.

Create e.g. temp_N_def_arg1 = call_arg1_label_visitor.result for each argument.
Visit the arguments if they're calls. (save_def_args_in_temp)

I do not think I care about this one actually -- Create e.g. def_arg1 = temp_N_def_arg1 for each argument.
(create_local_scope_from_def_args)

Add RestoreNode to the end of the Nodes.

#### Arguments

node(ast.Call) : The node that calls the definition.
- `blackbox(bool)` - Whether or not it is a builtin or blackbox call.

#### Returns

- `call_node(BBorBInode)` - The call node.

### StmtVisitor().add_module

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L724)

```python
def add_module(
    module,
    module_or_package_name,
    local_names,
    import_alias_mapping,
    is_init=False,
    from_from=False,
    from_fdid=False,
):
```

#### Returns

The ExitNode that gets attached to the CFG of the class.

### StmtVisitor().add_to_definitions

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L115)

```python
def add_to_definitions(node):
```

### StmtVisitor().append_node

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L719)

```python
def append_node(node):
```

Append a node to the CFG and return it.

### StmtVisitor().assign_multi_target

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L355)

```python
def assign_multi_target(node, right_hand_side_variables):
```

### StmtVisitor().assign_tuple_target

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L289)

```python
def assign_tuple_target(target_nodes, value_nodes, right_hand_side_variables):
```

### StmtVisitor().assignment_call_node

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L438)

```python
def assignment_call_node(left_hand_label, ast_node):
```

Handle assignments that contain a function call on its right side.

### StmtVisitor().from_directory_import

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L820)

```python
def from_directory_import(
    module,
    real_names,
    local_names,
    import_alias_mapping,
    skip_init=False,
):
```

Directories don't need to be packages.

### StmtVisitor().get_parent_definitions

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L109)

```python
def get_parent_definitions():
```

### StmtVisitor().handle_or_else

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L161)

```python
def handle_or_else(orelse, test):
```

Handle the orelse part of an if or try node.

#### Arguments

orelse(list[Node])
test(Node)

#### Returns

The last nodes of the orelse branch.

### StmtVisitor().handle_relative_import

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L875)

```python
def handle_relative_import(node):
```

from A means node.level == 0
from . import B means node.level == 1
from .A means node.level == 1

### StmtVisitor().handle_stmt_star_ignore_node

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L237)

```python
def handle_stmt_star_ignore_node(body, fallback_cfg_node):
```

### StmtVisitor().import_package

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L862)

```python
def import_package(module, module_name, local_name, import_alias_mapping):
```

### StmtVisitor().loop_node_skeleton

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L473)

```python
def loop_node_skeleton(test, node):
```

Common handling of looped structures, while and for.

### StmtVisitor().process_loop_funcs

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L515)

```python
def process_loop_funcs(comp_n, loop_node):
```

If the loop test node contains function calls, it connects the loop node to the nodes of
those function calls.

#### Arguments

- `comp_n` - The test node of a loop that may contain functions.
- `loop_node` - The loop node itself to connect to the new function nodes if any

#### Returns

None

### StmtVisitor().stmt_star_handler

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L55)

```python
def stmt_star_handler(stmts, prev_node_to_avoid=None):
```

Handle stmt* expressions in an AST node.

Links all statements together in a list of statements, accounting for statements with multiple last nodes.

### StmtVisitor().visit_AnnAssign

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L430)

```python
def visit_AnnAssign(node):
```

### StmtVisitor().visit_Assert

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L690)

```python
def visit_Assert(node):
```

### StmtVisitor().visit_Assign

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L377)

```python
def visit_Assign(node):
```

### StmtVisitor().visit_AugAssign

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L458)

```python
def visit_AugAssign(node):
```

### StmtVisitor().visit_Break

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L680)

```python
def visit_Break(node):
```

### StmtVisitor().visit_ClassDef

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L138)

```python
def visit_ClassDef(node):
```

### StmtVisitor().visit_Continue

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L697)

```python
def visit_Continue(node):
```

### StmtVisitor().visit_Delete

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L683)

```python
def visit_Delete(node):
```

### StmtVisitor().visit_Expr

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L716)

```python
def visit_Expr(node):
```

### StmtVisitor().visit_For

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L498)

```python
def visit_For(node):
```

### StmtVisitor().visit_FunctionDef

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L156)

```python
def visit_FunctionDef(node):
```

### StmtVisitor().visit_Global

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L700)

```python
def visit_Global(node):
```

### StmtVisitor().visit_If

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L184)

```python
def visit_If(node):
```

### StmtVisitor().visit_Import

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L923)

```python
def visit_Import(node):
```

### StmtVisitor().visit_ImportFrom

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L961)

```python
def visit_ImportFrom(node):
```

### StmtVisitor().visit_Module

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L52)

```python
def visit_Module(node):
```

### StmtVisitor().visit_Pass

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L703)

```python
def visit_Pass(node):
```

### StmtVisitor().visit_Raise

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L207)

```python
def visit_Raise(node):
```

### StmtVisitor().visit_Return

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L210)

```python
def visit_Return(node):
```

### StmtVisitor().visit_Try

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L246)

```python
def visit_Try(node):
```

### StmtVisitor().visit_While

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L529)

```python
def visit_While(node):
```

### StmtVisitor().visit_With

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L668)

```python
def visit_With(node):
```

### StmtVisitor().visit_miscelleaneous_node

[[find in source code]](../../../pytaintx/cfg/stmt_visitor.py#L706)

```python
def visit_miscelleaneous_node(node, custom_label=None):
```
