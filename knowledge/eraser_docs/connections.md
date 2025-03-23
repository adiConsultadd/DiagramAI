# Diagram Connections

Connections in Eraser.io diagrams visually represent the relationships, data flows, or dependencies between nodes and groups. This document explains how to create and customize connections using the diagram-as-code language.

---

## Basic Connection Syntax

A connection is defined by writing the names of two nodes (or groups) separated by a connector symbol. For example:

```plaintext
Compute > Storage
```

This statement creates a left-to-right arrow from the node `Compute` to the node `Storage`.

---

## Connector Types

Eraser.io supports several types of connectors, each represented by a specific symbol:

- `>` : Left-to-right arrow
- `<` : Right-to-left arrow
- `<>` : Bi-directional arrow
- `-` : Plain line
- `--` : Dotted line
- `-->`: Dotted arrow

Choose the connector that best represents the relationship between your components.

---

## Adding Labels to Connections

You can add a label to a connection by appending a colon `:` followed by the label text. This helps clarify the nature of the connection. For example:

```plaintext
Storage > Server: Cache Hit
```

In this case, the label "Cache Hit" is displayed along the connection from `Storage` to `Server`.

---

## One-to-Many Connections

To connect a single node to multiple nodes in one statement, separate the target nodes with commas. For example:

```plaintext
Server > Worker1, Worker2, Worker3
```

This creates individual connections from `Server` to each of the `Worker` nodes.

---

## Implicit Node Creation

If a name in a connection is not previously defined as a node or group, Eraser.io automatically creates a blank node with that name. This allows you to quickly sketch out connections without needing to predefine every node.

---

## Connection Properties

Like nodes and groups, connections can be styled with properties. Properties are added at the end of the connection statement within square brackets. For example, to set the connection’s line color to green, use:

```plaintext
Storage > Server [color: green]
```

Alternatively, you can also place the properties immediately after the connection label:

```plaintext
Storage > Server: Cache Hit [color: green]
```

Connection properties can help differentiate data flows or emphasize critical relationships within your diagram.

---

This document covers the essential syntax for creating connections in Eraser.io diagrams. By combining the various connector types, labels, and properties, you can accurately represent complex relationships and data flows in your architecture diagrams.
