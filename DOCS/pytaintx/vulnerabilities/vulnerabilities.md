# vulnerabilities

> Auto-generated documentation for [pytaintx.vulnerabilities.vulnerabilities](../../../pytaintx/vulnerabilities/vulnerabilities.py) module.

Module for finding vulnerabilities based on a definitions file.

- [Pytaintx](../../README.md#pytaintx-index) / [Modules](../../README.md#pytaintx-modules) / [pytaintx](../index.md#pytaintx) / [vulnerabilities](index.md#vulnerabilities) / vulnerabilities
    - [append_node_if_reassigned](#append_node_if_reassigned)
    - [build_sanitiser_node_dict](#build_sanitiser_node_dict)
    - [filter_cfg_nodes](#filter_cfg_nodes)
    - [find_assignments](#find_assignments)
    - [find_sanitiser_nodes](#find_sanitiser_nodes)
    - [find_secondary_sources](#find_secondary_sources)
    - [find_triggers](#find_triggers)
    - [find_vulnerabilities](#find_vulnerabilities)
    - [find_vulnerabilities_in_cfg](#find_vulnerabilities_in_cfg)
    - [get_sink_args](#get_sink_args)
    - [get_sink_args_which_propagate](#get_sink_args_which_propagate)
    - [get_tainted_node_in_sink_args](#get_tainted_node_in_sink_args)
    - [get_vulnerability](#get_vulnerability)
    - [get_vulnerability_chains](#get_vulnerability_chains)
    - [how_vulnerable](#how_vulnerable)
    - [identify_triggers](#identify_triggers)
    - [label_contains](#label_contains)
    - [update_assignments](#update_assignments)

## append_node_if_reassigned

[[find in source code]](../../../pytaintx/vulnerabilities/vulnerabilities.py#L123)

```python
def append_node_if_reassigned(assignment_list, secondary, node):
```

## build_sanitiser_node_dict

[[find in source code]](../../../pytaintx/vulnerabilities/vulnerabilities.py#L176)

```python
def build_sanitiser_node_dict(cfg, sinks_in_file):
```

Build a dict of string -> TriggerNode pairs, where the string
is the sanitiser and the TriggerNode is a TriggerNode of the sanitiser.

#### Arguments

- `cfg(CFG)` - cfg to traverse.
- `sinks_in_file(list[TriggerNode])` - list of TriggerNodes containing
                                  the sinks in the file.

#### Returns

A string -> TriggerNode dict.

## filter_cfg_nodes

[[find in source code]](../../../pytaintx/vulnerabilities/vulnerabilities.py#L68)

```python
def filter_cfg_nodes(cfg, cfg_node_type):
```

## find_assignments

[[find in source code]](../../../pytaintx/vulnerabilities/vulnerabilities.py#L92)

```python
def find_assignments(assignment_nodes, source, lattice):
```

## find_sanitiser_nodes

[[find in source code]](../../../pytaintx/vulnerabilities/vulnerabilities.py#L210)

```python
def find_sanitiser_nodes(sanitiser, sanitisers_in_file):
```

Find nodes containing a particular sanitiser.

#### Arguments

- `sanitiser(string)` - sanitiser to look for.
- `sanitisers_in_file(list[Node])` - list of CFG nodes with the sanitiser.

#### Returns

Iterable of sanitiser nodes.

## find_secondary_sources

[[find in source code]](../../../pytaintx/vulnerabilities/vulnerabilities.py#L75)

```python
def find_secondary_sources(assignment_nodes, sources, lattice):
```

Sets the secondary_nodes attribute of each source in the sources list.

#### Arguments

assignment_nodes([AssignmentNode])
sources([tuple])
- `lattice(Lattice)` - the lattice we're analysing.

## find_triggers

[[find in source code]](../../../pytaintx/vulnerabilities/vulnerabilities.py#L135)

```python
def find_triggers(nodes, trigger_words, nosec_lines):
```

Find triggers from the trigger_word_list in the nodes.

#### Arguments

- `nodes(list[Node])` - the nodes to find triggers in.
- `trigger_word_list(list[Union[Sink,` *Source]])* - list of trigger words to look for.
- `nosec_lines(set)` - lines with # nosec whitelisting

#### Returns

List of found TriggerNodes

## find_vulnerabilities

[[find in source code]](../../../pytaintx/vulnerabilities/vulnerabilities.py#L512)

```python
def find_vulnerabilities(
    cfg_list,
    blackbox_mapping_file,
    sources_and_sinks_file,
    interactive=False,
    nosec_lines=defaultdict(set),
):
```

Find vulnerabilities in a list of CFGs from a trigger_word_file.

#### Arguments

- `cfg_list(list[CFG])` - the list of CFGs to scan.
blackbox_mapping_file(str)
sources_and_sinks_file(str)
- `interactive(bool)` - determines if we ask the user about blackbox functions not in the mapping file.

#### Returns

A list of vulnerabilities.

## find_vulnerabilities_in_cfg

[[find in source code]](../../../pytaintx/vulnerabilities/vulnerabilities.py#L471)

```python
def find_vulnerabilities_in_cfg(
    cfg,
    definitions,
    lattice,
    blackbox_mapping,
    vulnerabilities_list,
    interactive,
    nosec_lines,
):
```

Find vulnerabilities in a cfg.

#### Arguments

- `cfg(CFG)` - The CFG to find vulnerabilities in.
- `definitions(trigger_definitions_parser.Definitions)` - Source and sink definitions.
- `lattice(Lattice)` - the lattice we're analysing.
- `blackbox_mapping(dict)` - A map of blackbox functions containing whether or not they propagate taint.
- `vulnerabilities_list(list)` - That we append to when we find vulnerabilities.
- `interactive(bool)` - determines if we ask the user about blackbox functions not in the mapping file.

## get_sink_args

[[find in source code]](../../../pytaintx/vulnerabilities/vulnerabilities.py#L228)

```python
def get_sink_args(cfg_node):
```

## get_sink_args_which_propagate

[[find in source code]](../../../pytaintx/vulnerabilities/vulnerabilities.py#L243)

```python
def get_sink_args_which_propagate(sink, ast_node):
```

## get_tainted_node_in_sink_args

[[find in source code]](../../../pytaintx/vulnerabilities/vulnerabilities.py#L364)

```python
def get_tainted_node_in_sink_args(sink_args, nodes_in_constraint):
```

## get_vulnerability

[[find in source code]](../../../pytaintx/vulnerabilities/vulnerabilities.py#L376)

```python
def get_vulnerability(
    source,
    sink,
    triggers,
    lattice,
    cfg,
    interactive,
    blackbox_mapping,
):
```

Get vulnerability between source and sink if it exists.

Uses triggers to find sanitisers.

Note: When a secondary node is in_constraint with the sink
          but not the source, the secondary is a save_N_LHS
          node made in process_function in expr_visitor.

#### Arguments

- `source(TriggerNode)` - TriggerNode of the source.
- `sink(TriggerNode)` - TriggerNode of the sink.
- `triggers(Triggers)` - Triggers of the CFG.
- `lattice(Lattice)` - the lattice we're analysing.
- `cfg(CFG)` - .blackbox_assignments used in is_unknown, .nodes used in build_def_use_chain
- `interactive(bool)` - determines if we ask the user about blackbox functions not in the mapping file.
- `blackbox_mapping(dict)` - A map of blackbox functions containing whether or not they propagate taint.

#### Returns

A Vulnerability if it exists, else None

## get_vulnerability_chains

[[find in source code]](../../../pytaintx/vulnerabilities/vulnerabilities.py#L272)

```python
def get_vulnerability_chains(current_node, sink, def_use, chain=[]):
```

Traverses the def-use graph to find all paths from source to sink that cause a vulnerability.

#### Arguments

current_node()
sink()
def_use(dict):
- `chain(list(Node))` - A path of nodes between source and sink.

## how_vulnerable

[[find in source code]](../../../pytaintx/vulnerabilities/vulnerabilities.py#L300)

```python
def how_vulnerable(
    chain,
    blackbox_mapping,
    sanitiser_nodes,
    potential_sanitiser,
    blackbox_assignments,
    interactive,
    vuln_deets,
):
```

Iterates through the chain of nodes and checks the blackbox nodes against the blackbox mapping and sanitiser dictionary.

Note: potential_sanitiser is the only hack here, it is because we do not take p-use's into account yet.
e.g. we can only say potentially instead of definitely sanitised in the path_traversal_sanitised_2.py test.

#### Arguments

- `chain(list(Node))` - A path of nodes between source and sink.
- `blackbox_mapping(dict)` - A map of blackbox functions containing whether or not they propagate taint.
- `sanitiser_nodes(set)` - A set of nodes that are sanitisers for the sink.
- `potential_sanitiser(Node)` - An if or elif node that can potentially cause sanitisation.
- `blackbox_assignments(set[AssignmentNode])` - set of blackbox assignments, includes the ReturnNode's of BBorBInode's.
- `interactive(bool)` - determines if we ask the user about blackbox functions not in the mapping file.
- `vuln_deets(dict)` - vulnerability details.

#### Returns

A VulnerabilityType depending on how vulnerable the chain is.

## identify_triggers

[[find in source code]](../../../pytaintx/vulnerabilities/vulnerabilities.py#L30)

```python
def identify_triggers(cfg, sources, sinks, lattice, nosec_lines):
```

Identify sources, sinks and sanitisers in a CFG.

#### Arguments

- `cfg(CFG)` - CFG to find sources, sinks and sanitisers in.
- `sources(tuple)` - list of sources, a source is a (source, sanitiser) tuple.
- `sinks(tuple)` - list of sources, a sink is a (sink, sanitiser) tuple.
- `nosec_lines(set)` - lines with # nosec whitelisting

#### Returns

Triggers tuple with sink and source nodes and a sanitiser node dict.

## label_contains

[[find in source code]](../../../pytaintx/vulnerabilities/vulnerabilities.py#L157)

```python
def label_contains(node, triggers):
```

Determine if node contains any of the trigger_words provided.

#### Arguments

- `node(Node)` - CFG node to check.
- `trigger_words(list[Union[Sink,` *Source]])* - list of trigger words to look for.

#### Returns

Iterable of TriggerNodes found. Can be multiple because multiple
trigger_words can be in one node.

## update_assignments

[[find in source code]](../../../pytaintx/vulnerabilities/vulnerabilities.py#L111)

```python
def update_assignments(assignment_list, assignment_nodes, source, lattice):
```
