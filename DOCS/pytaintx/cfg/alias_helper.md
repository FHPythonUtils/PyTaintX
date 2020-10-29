# alias_helper

> Auto-generated documentation for [pytaintx.cfg.alias_helper](../../../pytaintx/cfg/alias_helper.py) module.

This module contains alias helper functions for the expr_visitor module.

- [Pytaintx](../../README.md#pytaintx-index) / [Modules](../../README.md#pytaintx-modules) / [pytaintx](../index.md#pytaintx) / [cfg](index.md#cfg) / alias_helper
    - [as_alias_handler](#as_alias_handler)
    - [fully_qualify_alias_labels](#fully_qualify_alias_labels)
    - [handle_aliases_in_calls](#handle_aliases_in_calls)
    - [handle_aliases_in_init_files](#handle_aliases_in_init_files)
    - [handle_fdid_aliases](#handle_fdid_aliases)
    - [not_as_alias_handler](#not_as_alias_handler)
    - [retrieve_import_alias_mapping](#retrieve_import_alias_mapping)

## as_alias_handler

[[find in source code]](../../../pytaintx/cfg/alias_helper.py#L4)

```python
def as_alias_handler(alias_list):
```

Returns a list of all the names that will be called.

## fully_qualify_alias_labels

[[find in source code]](../../../pytaintx/cfg/alias_helper.py#L79)

```python
def fully_qualify_alias_labels(label, aliases):
```

Replace any aliases in label with the fully qualified name.

#### Arguments

- `label` - A label : str representing a name (e.g. myos.system)
- `aliases` - A dict of {alias: real_name} (e.g. {'myos': 'os'})

```python
>>> fully_qualify_alias_labels('myos.mycall', {'myos':'os'})
'os.mycall'

## handle_aliases_in_calls

[[find in source code]](../../../pytaintx/cfg/alias_helper.py#L15)

```python
def handle_aliases_in_calls(name, import_alias_mapping):
```

Returns either None or the handled alias.
Used in add_module.

## handle_aliases_in_init_files

[[find in source code]](../../../pytaintx/cfg/alias_helper.py#L32)

```python
def handle_aliases_in_init_files(name, import_alias_mapping):
```

Returns either None or the handled alias.
Used in add_module.

## handle_fdid_aliases

[[find in source code]](../../../pytaintx/cfg/alias_helper.py#L49)

```python
def handle_fdid_aliases(module_or_package_name, import_alias_mapping):
```

Returns either None or the handled alias.
Used in add_module.
fdid means from directory import directory.

## not_as_alias_handler

[[find in source code]](../../../pytaintx/cfg/alias_helper.py#L60)

```python
def not_as_alias_handler(names_list):
```

Returns a list of names ignoring any aliases.

## retrieve_import_alias_mapping

[[find in source code]](../../../pytaintx/cfg/alias_helper.py#L68)

```python
def retrieve_import_alias_mapping(names_list):
```

Creates a dictionary mapping aliases to their respective name.
import_alias_names is used in module_definitions.py and visit_Call
