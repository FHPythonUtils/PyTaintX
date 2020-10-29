# text

> Auto-generated documentation for [pytaintx.formatters.text](../../../pytaintx/formatters/text.py) module.

This formatter outputs the issues as plain text.

- [Pytaintx](../../README.md#pytaintx-index) / [Modules](../../README.md#pytaintx-modules) / [pytaintx](../index.md#pytaintx) / [formatters](index.md#formatters) / text
    - [report](#report)

## report

[[find in source code]](../../../pytaintx/formatters/text.py#L5)

```python
def report(vulnerabilities, fileobj, print_sanitised):
```

Prints issues in text format.

#### Arguments

- `vulnerabilities` - list of vulnerabilities to report
- `fileobj` - The output file object, which may be sys.stdout
- `print_sanitised` - Print just unsanitised vulnerabilities or sanitised vulnerabilities as well
