# trigger_definitions_parser

> Auto-generated documentation for [pytaintx.vulnerabilities.trigger_definitions_parser](../../../pytaintx/vulnerabilities/trigger_definitions_parser.py) module.

- [Pytaintx](../../README.md#pytaintx-index) / [Modules](../../README.md#pytaintx-modules) / [pytaintx](../index.md#pytaintx) / [vulnerabilities](index.md#vulnerabilities) / trigger_definitions_parser
    - [Sink](#sink)
        - [Sink().all_arguments_propagate_taint](#sinkall_arguments_propagate_taint)
        - [Sink().arg_propagates](#sinkarg_propagates)
        - [Sink().call](#sinkcall)
        - [Sink.from_json](#sinkfrom_json)
        - [Sink().get_kwarg_from_position](#sinkget_kwarg_from_position)
        - [Sink().kwarg_propagates](#sinkkwarg_propagates)
        - [Sink().trigger_word](#sinktrigger_word)
    - [parse](#parse)

## Sink

[[find in source code]](../../../pytaintx/vulnerabilities/trigger_definitions_parser.py#L16)

```python
class Sink():
    def __init__(
        trigger,
        unlisted_args_propagate=True,
        arg_dict=None,
        sanitisers=None,
    ):
```

### Sink().all_arguments_propagate_taint

[[find in source code]](../../../pytaintx/vulnerabilities/trigger_definitions_parser.py#L48)

```python
@property
def all_arguments_propagate_taint():
```

### Sink().arg_propagates

[[find in source code]](../../../pytaintx/vulnerabilities/trigger_definitions_parser.py#L37)

```python
def arg_propagates(index):
```

### Sink().call

[[find in source code]](../../../pytaintx/vulnerabilities/trigger_definitions_parser.py#L54)

```python
@property
def call():
```

### Sink.from_json

[[find in source code]](../../../pytaintx/vulnerabilities/trigger_definitions_parser.py#L64)

```python
@classmethod
def from_json(key, data):
```

### Sink().get_kwarg_from_position

[[find in source code]](../../../pytaintx/vulnerabilities/trigger_definitions_parser.py#L45)

```python
def get_kwarg_from_position(index):
```

### Sink().kwarg_propagates

[[find in source code]](../../../pytaintx/vulnerabilities/trigger_definitions_parser.py#L41)

```python
def kwarg_propagates(keyword):
```

### Sink().trigger_word

[[find in source code]](../../../pytaintx/vulnerabilities/trigger_definitions_parser.py#L60)

```python
@property
def trigger_word():
```

## parse

[[find in source code]](../../../pytaintx/vulnerabilities/trigger_definitions_parser.py#L69)

```python
def parse(trigger_word_file):
```

Parse the file for source and sink definitions.

#### Returns

A definitions tuple with sources and sinks.
