# screen

> Auto-generated documentation for [pytaintx.formatters.screen](../../../pytaintx/formatters/screen.py) module.

This formatter outputs the issues as color-coded text.

- [Pytaintx](../../README.md#pytaintx-index) / [Modules](../../README.md#pytaintx-modules) / [pytaintx](../index.md#pytaintx) / [formatters](index.md#formatters) / screen
    - [color](#color)
    - [report](#report)
    - [vulnerability_to_str](#vulnerability_to_str)

## color

[[find in source code]](../../../pytaintx/formatters/screen.py#L13)

```python
def color(string, color_string):
```

## report

[[find in source code]](../../../pytaintx/formatters/screen.py#L17)

```python
def report(vulnerabilities, fileobj, print_sanitised):
```

Prints issues in color-coded text format.

#### Arguments

- `vulnerabilities` - list of vulnerabilities to report
- `fileobj` - The output file object, which may be sys.stdout

## vulnerability_to_str

[[find in source code]](../../../pytaintx/formatters/screen.py#L49)

```python
def vulnerability_to_str(i, vulnerability):
```
