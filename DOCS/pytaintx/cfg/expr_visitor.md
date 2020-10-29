# expr_visitor

> Auto-generated documentation for [pytaintx.cfg.expr_visitor](../../../pytaintx/cfg/expr_visitor.py) module.

- [Pytaintx](../../README.md#pytaintx-index) / [Modules](../../README.md#pytaintx-modules) / [pytaintx](../index.md#pytaintx) / [cfg](index.md#cfg) / expr_visitor
    - [ExprVisitor](#exprvisitor)
        - [ExprVisitor().connect_if_allowed](#exprvisitorconnect_if_allowed)
        - [ExprVisitor().create_local_scope_from_def_args](#exprvisitorcreate_local_scope_from_def_args)
        - [ExprVisitor().init_cfg](#exprvisitorinit_cfg)
        - [ExprVisitor().init_function_cfg](#exprvisitorinit_function_cfg)
        - [ExprVisitor().process_function](#exprvisitorprocess_function)
        - [ExprVisitor().restore_saved_local_scope](#exprvisitorrestore_saved_local_scope)
        - [ExprVisitor().return_handler](#exprvisitorreturn_handler)
        - [ExprVisitor().save_def_args_in_temp](#exprvisitorsave_def_args_in_temp)
        - [ExprVisitor().save_local_scope](#exprvisitorsave_local_scope)
        - [ExprVisitor().visit_Attribute](#exprvisitorvisit_attribute)
        - [ExprVisitor().visit_Call](#exprvisitorvisit_call)
        - [ExprVisitor().visit_Name](#exprvisitorvisit_name)
        - [ExprVisitor().visit_NameConstant](#exprvisitorvisit_nameconstant)
        - [ExprVisitor().visit_Str](#exprvisitorvisit_str)
        - [ExprVisitor().visit_Subscript](#exprvisitorvisit_subscript)
        - [ExprVisitor().visit_Tuple](#exprvisitorvisit_tuple)
        - [ExprVisitor().visit_Yield](#exprvisitorvisit_yield)
        - [ExprVisitor().visit_YieldFrom](#exprvisitorvisit_yieldfrom)
        - [ExprVisitor().visit_and_get_function_nodes](#exprvisitorvisit_and_get_function_nodes)

## ExprVisitor

[[find in source code]](../../../pytaintx/cfg/expr_visitor.py#L38)

```python
class ExprVisitor(StmtVisitor):
    def __init__(
        node,
        project_modules,
        local_modules,
        filename,
        module_definitions=None,
        allow_local_directory_imports=True,
    ):
```

### ExprVisitor().connect_if_allowed

[[find in source code]](../../../pytaintx/cfg/expr_visitor.py#L170)

```python
def connect_if_allowed(previous_node, node_to_connect_to):
```

### ExprVisitor().create_local_scope_from_def_args

[[find in source code]](../../../pytaintx/cfg/expr_visitor.py#L331)

```python
def create_local_scope_from_def_args(
    call_args,
    def_args,
    line_number,
    saved_function_call_index,
):
```

Create the local scope before entering the body of a function call.

#### Arguments

- `call_args(list[ast.Name])` - Of the call being made.
- `def_args(ast_helper.Arguments)` - Of the definition being called.
- `line_number(int)` - Of the def of the function call about to be entered into.
- `saved_function_call_index(int)` - Unique number for each call.

- `Note` - We do not need a connect_if_allowed because of the
      preceding call to save_def_args_in_temp.

### ExprVisitor().init_cfg

[[find in source code]](../../../pytaintx/cfg/expr_visitor.py#L71)

```python
def init_cfg(node):
```

### ExprVisitor().init_function_cfg

[[find in source code]](../../../pytaintx/cfg/expr_visitor.py#L96)

```python
def init_function_cfg(node, module_definitions):
```

### ExprVisitor().process_function

[[find in source code]](../../../pytaintx/cfg/expr_visitor.py#L485)

```python
def process_function(call_node, definition):
```

Processes a user defined function when it is called.

Increments self.function_call_index each time it is called, we can refer to it as N in the comments.
Make e.g. save_N_LHS = assignment.LHS for each AssignmentNode. (save_local_scope)
Create e.g. temp_N_def_arg1 = call_arg1_label_visitor.result for each argument.
    Visit the arguments if they're calls. (save_def_args_in_temp)
Create e.g. def_arg1 = temp_N_def_arg1 for each argument. (create_local_scope_from_def_args)
Visit and get function nodes. (visit_and_get_function_nodes)
Loop through each save_N_LHS node and create an e.g.
    foo = save_1_foo or, if foo was a call arg, foo = arg_mapping[foo]. (restore_saved_local_scope)
Create e.g. ~call_1 = ret_func_foo RestoreNode. (return_handler)

#### Notes

Page 31 in the original thesis, but changed a little.
We don't have to return the ~call_1 = ret_func_foo RestoreNode made in return_handler,
    because it's the last node anyway, that we return in this function.
e.g. ret_func_foo gets assigned to visit_Return.

#### Arguments

call_node(ast.Call) : The node that calls the definition.
- `definition(LocalModuleDefinition)` - Definition of the function being called.

#### Returns

Last node in self.nodes, probably the return of the function appended to self.nodes in return_handler.

### ExprVisitor().restore_saved_local_scope

[[find in source code]](../../../pytaintx/cfg/expr_visitor.py#L398)

```python
def restore_saved_local_scope(saved_variables, args_mapping, line_number):
```

Restore the previously saved variables to their original values.

#### Arguments

saved_variables(list[SavedVariable])
- `args_mapping(dict)` - A mapping of call argument to definition argument.
- `line_number(int)` - Of the def of the function call about to be entered into.

- `Note` - We do not need connect_if_allowed because of the
      preceding call to save_local_scope.

### ExprVisitor().return_handler

[[find in source code]](../../../pytaintx/cfg/expr_visitor.py#L447)

```python
def return_handler(
    call_node,
    function_nodes,
    saved_function_call_index,
    first_node,
):
```

Handle the return from a function during a function call.

#### Arguments

call_node(ast.Call) : The node that calls the definition.
- `function_nodes(list[Node])` - List of nodes of the function being called.
- `saved_function_call_index(int)` - Unique number for each call.
first_node(EntryOrExitNode or RestoreNode): Used to connect previous statements to this function.

### ExprVisitor().save_def_args_in_temp

[[find in source code]](../../../pytaintx/cfg/expr_visitor.py#L247)

```python
def save_def_args_in_temp(
    call_args,
    def_args,
    line_number,
    saved_function_call_index,
    first_node,
):
```

Save the arguments of the definition being called. Visit the arguments if they're calls.

#### Arguments

- `call_args(list[ast.Name])` - Of the call being made.
- `def_args(ast_helper.Arguments)` - Of the definition being called.
- `line_number(int)` - Of the call being made.
- `saved_function_call_index(int)` - Unique number for each call.
first_node(EntryOrExitNode or None or RestoreNode): Used to connect previous statements to this function.

#### Returns

- `args_mapping(dict)` - A mapping of call argument to definition argument.
first_node(EntryOrExitNode or None or RestoreNode): Used to connect previous statements to this function.

### ExprVisitor().save_local_scope

[[find in source code]](../../../pytaintx/cfg/expr_visitor.py#L198)

```python
def save_local_scope(line_number, saved_function_call_index):
```

Save the local scope before entering a function call by saving all the LHS's of assignments so far.

#### Arguments

- `line_number(int)` - Of the def of the function call about to be entered into.
- `saved_function_call_index(int)` - Unique number for each call.

#### Returns

saved_variables(list[SavedVariable])
first_node(EntryOrExitNode or None or RestoreNode): Used to connect previous statements to this function.

### ExprVisitor().visit_Attribute

[[find in source code]](../../../pytaintx/cfg/expr_visitor.py#L142)

```python
def visit_Attribute(node):
```

### ExprVisitor().visit_Call

[[find in source code]](../../../pytaintx/cfg/expr_visitor.py#L556)

```python
def visit_Call(node):
```

### ExprVisitor().visit_Name

[[find in source code]](../../../pytaintx/cfg/expr_visitor.py#L147)

```python
def visit_Name(node):
```

### ExprVisitor().visit_NameConstant

[[find in source code]](../../../pytaintx/cfg/expr_visitor.py#L152)

```python
def visit_NameConstant(node):
```

### ExprVisitor().visit_Str

[[find in source code]](../../../pytaintx/cfg/expr_visitor.py#L157)

```python
def visit_Str(node):
```

### ExprVisitor().visit_Subscript

[[find in source code]](../../../pytaintx/cfg/expr_visitor.py#L160)

```python
def visit_Subscript(node):
```

### ExprVisitor().visit_Tuple

[[find in source code]](../../../pytaintx/cfg/expr_visitor.py#L165)

```python
def visit_Tuple(node):
```

### ExprVisitor().visit_Yield

[[find in source code]](../../../pytaintx/cfg/expr_visitor.py#L119)

```python
def visit_Yield(node):
```

### ExprVisitor().visit_YieldFrom

[[find in source code]](../../../pytaintx/cfg/expr_visitor.py#L139)

```python
def visit_YieldFrom(node):
```

### ExprVisitor().visit_and_get_function_nodes

[[find in source code]](../../../pytaintx/cfg/expr_visitor.py#L364)

```python
def visit_and_get_function_nodes(definition, first_node):
```

Visits the nodes of a user defined function.

#### Arguments

- `definition(LocalModuleDefinition)` - Definition of the function being added.
first_node(EntryOrExitNode or None or RestoreNode): Used to connect previous statements to this function.

#### Returns

- `the_new_nodes(list[Node])` - The nodes added while visiting the function.
first_node(EntryOrExitNode or None or RestoreNode): Used to connect previous statements to this function.
