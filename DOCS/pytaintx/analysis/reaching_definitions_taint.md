# reaching_definitions_taint

> Auto-generated documentation for [pytaintx.analysis.reaching_definitions_taint](../../../pytaintx/analysis/reaching_definitions_taint.py) module.

- [Pytaintx](../../README.md#pytaintx-index) / [Modules](../../README.md#pytaintx-modules) / [pytaintx](../index.md#pytaintx) / [analysis](index.md#analysis) / reaching_definitions_taint
    - [ReachingDefinitionsTaintAnalysis](#reachingdefinitionstaintanalysis)
        - [ReachingDefinitionsTaintAnalysis().arrow](#reachingdefinitionstaintanalysisarrow)
        - [ReachingDefinitionsTaintAnalysis().dep](#reachingdefinitionstaintanalysisdep)
        - [ReachingDefinitionsTaintAnalysis().fixpointmethod](#reachingdefinitionstaintanalysisfixpointmethod)
        - [ReachingDefinitionsTaintAnalysis().join](#reachingdefinitionstaintanalysisjoin)

## ReachingDefinitionsTaintAnalysis

[[find in source code]](../../../pytaintx/analysis/reaching_definitions_taint.py#L9)

```python
class ReachingDefinitionsTaintAnalysis():
    def __init__(cfg):
```

### ReachingDefinitionsTaintAnalysis().arrow

[[find in source code]](../../../pytaintx/analysis/reaching_definitions_taint.py#L39)

```python
def arrow(JOIN, _id):
```

Removes all previous assignments from JOIN that have the same left hand side.
This represents the arrow id definition from Schwartzbach.

### ReachingDefinitionsTaintAnalysis().dep

[[find in source code]](../../../pytaintx/analysis/reaching_definitions_taint.py#L48)

```python
def dep(q_1):
```

Represents the dep mapping from Schwartzbach.

### ReachingDefinitionsTaintAnalysis().fixpointmethod

[[find in source code]](../../../pytaintx/analysis/reaching_definitions_taint.py#L14)

```python
def fixpointmethod(cfg_node):
```

The most important part of PyT, where we perform
the variant of reaching definitions to find where sources reach.

### ReachingDefinitionsTaintAnalysis().join

[[find in source code]](../../../pytaintx/analysis/reaching_definitions_taint.py#L34)

```python
def join(cfg_node):
```

Joins all constraints of the ingoing nodes and returns them.
This represents the JOIN auxiliary definition from Schwartzbach.
