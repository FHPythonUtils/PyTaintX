# lattice

> Auto-generated documentation for [pytaintx.analysis.lattice](../../../pytaintx/analysis/lattice.py) module.

- [Pytaintx](../../README.md#pytaintx-index) / [Modules](../../README.md#pytaintx-modules) / [pytaintx](../index.md#pytaintx) / [analysis](index.md#analysis) / lattice
    - [Lattice](#lattice)
        - [Lattice().get_elements](#latticeget_elements)
        - [Lattice().in_constraint](#latticein_constraint)
    - [get_lattice_elements](#get_lattice_elements)

## Lattice

[[find in source code]](../../../pytaintx/analysis/lattice.py#L14)

```python
class Lattice():
    def __init__(cfg_nodes):
```

### Lattice().get_elements

[[find in source code]](../../../pytaintx/analysis/lattice.py#L23)

```python
def get_elements(number):
```

### Lattice().in_constraint

[[find in source code]](../../../pytaintx/analysis/lattice.py#L36)

```python
def in_constraint(node1, node2):
```

Checks if node1 is in node2's constraints
For instance, if node1 = 010 and node2 = 110:
010 & 110 = 010 -> has the element.

## get_lattice_elements

[[find in source code]](../../../pytaintx/analysis/lattice.py#L5)

```python
def get_lattice_elements(cfg_nodes):
```

Returns all assignment nodes as they are the only lattice elements
in the reaching definitions analysis.
