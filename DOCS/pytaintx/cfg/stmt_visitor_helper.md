# stmt_visitor_helper

> Auto-generated documentation for [pytaintx.cfg.stmt_visitor_helper](../../../pytaintx/cfg/stmt_visitor_helper.py) module.

- [Pytaintx](../../README.md#pytaintx-index) / [Modules](../../README.md#pytaintx-modules) / [pytaintx](../index.md#pytaintx) / [cfg](index.md#cfg) / stmt_visitor_helper
    - [connect_nodes](#connect_nodes)
    - [extract_left_hand_side](#extract_left_hand_side)
    - [get_first_node](#get_first_node)
    - [get_first_statement](#get_first_statement)
    - [get_last_statements](#get_last_statements)
    - [remove_breaks](#remove_breaks)

## connect_nodes

[[find in source code]](../../../pytaintx/cfg/stmt_visitor_helper.py#L61)

```python
def connect_nodes(nodes):
```

Connect the nodes in a list linearly.

## extract_left_hand_side

[[find in source code]](../../../pytaintx/cfg/stmt_visitor_helper.py#L88)

```python
def extract_left_hand_side(target):
```

Extract the left hand side variable from a target.

Removes list indexes, stars and other left hand side elements.

## get_first_node

[[find in source code]](../../../pytaintx/cfg/stmt_visitor_helper.py#L103)

```python
def get_first_node(node, node_not_to_step_past):
```

This is a super hacky way of getting the first node after a statement.
We do this because we visit a statement and keep on visiting and get something in return that is rarely the first node.
So we loop and loop backwards until we hit the statement or there is nothing to step back to.

## get_first_statement

[[find in source code]](../../../pytaintx/cfg/stmt_visitor_helper.py#L128)

```python
def get_first_statement(node_or_tuple):
```

Find the first statement of the provided object.

#### Returns

The first element in the tuple if it is a tuple.
The node if it is a node.

## get_last_statements

[[find in source code]](../../../pytaintx/cfg/stmt_visitor_helper.py#L141)

```python
def get_last_statements(cfg_statements):
```

Retrieve the last statements from a cfg_statements list.

## remove_breaks

[[find in source code]](../../../pytaintx/cfg/stmt_visitor_helper.py#L149)

```python
def remove_breaks(last_statements):
```

Remove all break statements in last_statements.
