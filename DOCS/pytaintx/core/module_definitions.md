# module_definitions

> Auto-generated documentation for [pytaintx.core.module_definitions](../../../pytaintx/core/module_definitions.py) module.

This module handles module definitions
which basically is a list of module definition.

- [Pytaintx](../../README.md#pytaintx-index) / [Modules](../../README.md#pytaintx-modules) / [pytaintx](../index.md#pytaintx) / [core](index.md#core) / module_definitions
    - [LocalModuleDefinition](#localmoduledefinition)
    - [ModuleDefinition](#moduledefinition)
    - [ModuleDefinitions](#moduledefinitions)
        - [ModuleDefinitions().append_if_local_or_in_imports](#moduledefinitionsappend_if_local_or_in_imports)
        - [ModuleDefinitions().get_definition](#moduledefinitionsget_definition)
        - [ModuleDefinitions().set_definition_node](#moduledefinitionsset_definition_node)

#### Attributes

- `project_definitions` - Contains all project definitions for a program run
  Only used in framework_adaptor.py, but modified here: `dict()`

## LocalModuleDefinition

[[find in source code]](../../../pytaintx/core/module_definitions.py#L48)

```python
class LocalModuleDefinition(ModuleDefinition):
```

A local definition.

#### See also

- [ModuleDefinition](#moduledefinition)

## ModuleDefinition

[[find in source code]](../../../pytaintx/core/module_definitions.py#L12)

```python
class ModuleDefinition():
    def __init__(local_module_definitions, name, parent_module_name, path):
```

Handling of a definition.

## ModuleDefinitions

[[find in source code]](../../../pytaintx/core/module_definitions.py#L53)

```python
class ModuleDefinitions():
    def __init__(
        import_names=None,
        module_name=None,
        is_init=False,
        filename=None,
    ):
```

A collection of module definition.

Adds to the project definitions list.

### ModuleDefinitions().append_if_local_or_in_imports

[[find in source code]](../../../pytaintx/core/module_definitions.py#L79)

```python
def append_if_local_or_in_imports(definition):
```

Add definition to list.

Handles local definitions and adds to project_definitions.

### ModuleDefinitions().get_definition

[[find in source code]](../../../pytaintx/core/module_definitions.py#L100)

```python
def get_definition(name):
```

Get definitions by name.

### ModuleDefinitions().set_definition_node

[[find in source code]](../../../pytaintx/core/module_definitions.py#L106)

```python
def set_definition_node(node, name):
```

Set definition by name.
