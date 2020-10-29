# node_types

> Auto-generated documentation for [pytaintx.core.node_types](../../../pytaintx/core/node_types.py) module.

This module contains all of the CFG nodes types.

- [Pytaintx](../../README.md#pytaintx-index) / [Modules](../../README.md#pytaintx-modules) / [pytaintx](../index.md#pytaintx) / [core](index.md#core) / node_types
    - [AssignmentCallNode](#assignmentcallnode)
    - [AssignmentNode](#assignmentnode)
    - [BBorBInode](#bborbinode)
    - [BreakNode](#breaknode)
    - [ConnectToExitNode](#connecttoexitnode)
    - [EntryOrExitNode](#entryorexitnode)
    - [IfNode](#ifnode)
    - [IgnoredNode](#ignorednode)
    - [Node](#node)
        - [Node().\_\_repr\_\_](#node__repr__)
        - [Node().\_\_str\_\_](#node__str__)
        - [Node().as_dict](#nodeas_dict)
        - [Node().connect](#nodeconnect)
        - [Node().connect_predecessors](#nodeconnect_predecessors)
    - [RaiseNode](#raisenode)
    - [RestoreNode](#restorenode)
    - [ReturnNode](#returnnode)
    - [TaintedNode](#taintednode)
    - [TryNode](#trynode)
    - [YieldNode](#yieldnode)

## AssignmentCallNode

[[find in source code]](../../../pytaintx/core/node_types.py#L222)

```python
class AssignmentCallNode(AssignmentNode):
    def __init__(
        label,
        left_hand_side,
        ast_node,
        right_hand_side_variables,
        line_number,
        path,
        call_node,
    ):
```

Node used for when a call happens inside of an assignment.

#### See also

- [AssignmentNode](#assignmentnode)

## AssignmentNode

[[find in source code]](../../../pytaintx/core/node_types.py#L152)

```python
class AssignmentNode(Node):
    def __init__(
        label,
        left_hand_side,
        ast_node,
        right_hand_side_variables,
        line_number=None,
        path,
    ):
```

CFG Node that represents an assignment.

#### See also

- [Node](#node)

## BBorBInode

[[find in source code]](../../../pytaintx/core/node_types.py#L202)

```python
class BBorBInode(AssignmentNode):
    def __init__(
        label,
        left_hand_side,
        ast_node,
        right_hand_side_variables,
        line_number,
        path,
        func_name,
    ):
```

Node used for handling restore nodes returning from blackbox or builtin function calls.

#### See also

- [AssignmentNode](#assignmentnode)

## BreakNode

[[find in source code]](../../../pytaintx/core/node_types.py#L95)

```python
class BreakNode(Node):
    def __init__(ast_node, path):
```

CFG Node that represents a Break statement.

#### See also

- [Node](#node)

## ConnectToExitNode

[[find in source code]](../../../pytaintx/core/node_types.py#L22)

```python
class ConnectToExitNode():
```

A common type between raise's and return's, used in return_handler.

## EntryOrExitNode

[[find in source code]](../../../pytaintx/core/node_types.py#L131)

```python
class EntryOrExitNode(Node):
    def __init__(label):
```

CFG Node that represents an Exit or an Entry node.

#### See also

- [Node](#node)

## IfNode

[[find in source code]](../../../pytaintx/core/node_types.py#L106)

```python
class IfNode(Node):
    def __init__(test_node, ast_node, path):
```

CFG Node that represents an If statement.

#### See also

- [Node](#node)

## IgnoredNode

[[find in source code]](../../../pytaintx/core/node_types.py#L17)

```python
class IgnoredNode():
```

Ignored Node sent from an ast node that should not return anything.

## Node

[[find in source code]](../../../pytaintx/core/node_types.py#L27)

```python
class Node():
    def __init__(label, ast_node, line_number=None, path):
```

A Control Flow Graph node that contains a list of
ingoing and outgoing nodes and a list of its variables.

### Node().\_\_repr\_\_

[[find in source code]](../../../pytaintx/core/node_types.py#L76)

```python
def __repr__():
```

Print a representation of the node.

### Node().\_\_str\_\_

[[find in source code]](../../../pytaintx/core/node_types.py#L72)

```python
def __str__():
```

Print the label of the node.

### Node().as_dict

[[find in source code]](../../../pytaintx/core/node_types.py#L50)

```python
def as_dict():
```

### Node().connect

[[find in source code]](../../../pytaintx/core/node_types.py#L57)

```python
def connect(successor):
```

Connect this node to its successor node by
setting its outgoing and the successors ingoing.

### Node().connect_predecessors

[[find in source code]](../../../pytaintx/core/node_types.py#L66)

```python
def connect_predecessors(predecessors):
```

Connect all nodes in predecessors to this node.

## RaiseNode

[[find in source code]](../../../pytaintx/core/node_types.py#L138)

```python
class RaiseNode(Node, ConnectToExitNode):
    def __init__(ast_node, path):
```

CFG Node that represents a Raise statement.

#### See also

- [ConnectToExitNode](#connecttoexitnode)
- [Node](#node)

## RestoreNode

[[find in source code]](../../../pytaintx/core/node_types.py#L186)

```python
class RestoreNode(AssignmentNode):
    def __init__(
        label,
        left_hand_side,
        right_hand_side_variables,
        line_number,
        path,
    ):
```

Node used for handling restore nodes returning from function calls.

#### See also

- [AssignmentNode](#assignmentnode)

## ReturnNode

[[find in source code]](../../../pytaintx/core/node_types.py#L259)

```python
class ReturnNode(AssignmentNode, ConnectToExitNode):
    def __init__(
        label,
        left_hand_side,
        ast_node,
        right_hand_side_variables,
        path,
    ):
```

CFG node that represents a return from a call.

#### See also

- [AssignmentNode](#assignmentnode)
- [ConnectToExitNode](#connecttoexitnode)

## TaintedNode

[[find in source code]](../../../pytaintx/core/node_types.py#L178)

```python
class TaintedNode(AssignmentNode):
```

CFG Node that represents a tainted node.

Only created in framework_adaptor.py and only used in `identify_triggers` of vulnerabilities.py

#### See also

- [AssignmentNode](#assignmentnode)

## TryNode

[[find in source code]](../../../pytaintx/core/node_types.py#L120)

```python
class TryNode(Node):
    def __init__(ast_node, path):
```

CFG Node that represents a Try statement.

#### See also

- [Node](#node)

## YieldNode

[[find in source code]](../../../pytaintx/core/node_types.py#L290)

```python
class YieldNode(AssignmentNode):
```

CFG Node that represents a yield or yield from.

The presence of a YieldNode means that a function is a generator.

#### See also

- [AssignmentNode](#assignmentnode)
