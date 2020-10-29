# json

> Auto-generated documentation for [pytaintx.formatters.json](../../../pytaintx/formatters/json.py) module.

This formatter outputs the issues in JSON.

- [Pytaintx](../../README.md#pytaintx-index) / [Modules](../../README.md#pytaintx-modules) / [pytaintx](../index.md#pytaintx) / [formatters](index.md#formatters) / json
    - [report](#report)

## report

[[find in source code]](../../../pytaintx/formatters/json.py#L8)

```python
def report(vulnerabilities, fileobj, print_sanitised):
```

Prints issues in JSON format.

#### Arguments

- `vulnerabilities` - list of vulnerabilities to report
- `fileobj` - The output file object, which may be sys.stdout
