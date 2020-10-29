# fixed_point

> Auto-generated documentation for [pytaintx.analysis.fixed_point](../../../pytaintx/analysis/fixed_point.py) module.

This module implements the fixed point algorithm.

- [Pytaintx](../../README.md#pytaintx-index) / [Modules](../../README.md#pytaintx-modules) / [pytaintx](../index.md#pytaintx) / [analysis](index.md#analysis) / fixed_point
    - [FixedPointAnalysis](#fixedpointanalysis)
        - [FixedPointAnalysis().fixpoint_runner](#fixedpointanalysisfixpoint_runner)
    - [analyse](#analyse)

## FixedPointAnalysis

[[find in source code]](../../../pytaintx/analysis/fixed_point.py#L6)

```python
class FixedPointAnalysis():
    def __init__(cfg):
```

Run the fix point analysis.

### FixedPointAnalysis().fixpoint_runner

[[find in source code]](../../../pytaintx/analysis/fixed_point.py#L17)

```python
def fixpoint_runner():
```

Work list algorithm that runs the fixpoint algorithm.

## analyse

[[find in source code]](../../../pytaintx/analysis/fixed_point.py#L33)

```python
def analyse(cfg_list):
```

Analyse a list of control flow graphs with a given analysis type.
