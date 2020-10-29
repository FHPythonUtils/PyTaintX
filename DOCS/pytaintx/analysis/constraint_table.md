# constraint_table

> Auto-generated documentation for [pytaintx.analysis.constraint_table](../../../pytaintx/analysis/constraint_table.py) module.

Global lookup table for constraints.

- [Pytaintx](../../README.md#pytaintx-index) / [Modules](../../README.md#pytaintx-modules) / [pytaintx](../index.md#pytaintx) / [analysis](index.md#analysis) / constraint_table
    - [constraint_join](#constraint_join)
    - [initialize_constraint_table](#initialize_constraint_table)

Uses cfg node as key and operates on bitvectors in the form of ints.

## constraint_join

[[find in source code]](../../../pytaintx/analysis/constraint_table.py#L14)

```python
def constraint_join(cfg_nodes):
```

Looks up all cfg_nodes and joins the bitvectors by using logical or.

## initialize_constraint_table

[[find in source code]](../../../pytaintx/analysis/constraint_table.py#L8)

```python
def initialize_constraint_table(cfg_list):
```

Collects all given cfg nodes and initializes the table with value 0.
