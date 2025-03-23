# Eraser Diagram Syntax

This document explains the core language used to write diagrams with Eraser.io. The syntax is designed to be simple and expressive while allowing you to define nodes, groups, properties, and connections.

---

## Nodes

A **node** is the most basic building block in a cloud architecture diagram. A node is defined by its unique name, optionally followed by a set of properties enclosed in square brackets. For example, the node below uses an AWS EC2 icon:

```plaintext
compute [icon: aws-ec2]
```

_Note:_

- **Node names must be unique.**
- Nodes support the following properties:
  - **icon:** Attaches an icon (e.g., `aws-ec2`)
  - **color:** Sets a stroke and fill color (either a name like `blue` or a hex code like `"#000000"`; note the quotes for hex codes)
  - **label:** Provides a custom text label, which can be used to override the node's name in the display (use quotes if the label contains spaces)
  - **colorMode:** Defines the fill color lightness; allowed values include `pastel`, `bold`, or `outline` (default is `pastel`)
  - **styleMode:** Chooses embellishments such as `shadow`, `plain`, or `watercolor` (default is `shadow`)
  - **typeface:** Sets the text style; allowed values include `rough`, `clean`, or `mono` (default is `rough`)

---

## Groups

A **group** is a container that encapsulates nodes and other groups. Groups are defined by a unique name followed by curly braces `{ }` that enclose its members. For example:

```plaintext
Main_Server {
  Server [icon: aws-ec2]
  Data [icon: aws-rds]
}
```

_Key Points:_

- **Group names must be unique.**
- Groups can be nested to represent hierarchical structures:

  ```plaintext
  VPC_Subnet {
    Main_Server {
      Server [icon: aws-ec2]
      Data [icon: aws-rds]
    }
  }
  ```

- Groups also support the same properties as nodes, such as `icon` and `color`.

---

## Properties

Properties are key-value pairs added within square brackets (`[ ]`) and can be appended to nodes or groups. Multiple properties are separated by commas. For example:

```plaintext
Server [icon: aws-ec2, color: blue, typeface: mono]
```

The allowed properties are:

| Property      | Description                                       | Example Value                   | Default Value   |
| ------------- | ------------------------------------------------- | ------------------------------- | --------------- |
| **icon**      | Attached icon name                                | `aws-ec2`                       | —               |
| **color**     | Stroke and fill color                             | `blue` or `"#000000"`           | —               |
| **label**     | Custom display label (if different from the name) | `"Main Server"`                 | Node/Group name |
| **colorMode** | Determines the fill color lightness               | `pastel`, `bold`, `outline`     | `pastel`        |
| **styleMode** | Sets embellishments                               | `shadow`, `plain`, `watercolor` | `shadow`        |
| **typeface**  | Sets the text typeface                            | `rough`, `clean`, `mono`        | `rough`         |

For a complete list of available icons, refer to the [Icons](#icons) section below.

---

## Connections

Connections represent relationships between nodes and groups, showing the flow of data or processes. They are defined using connector symbols between node names.

### Basic Connection Syntax

A simple connection uses an arrow, for example:

```plaintext
Compute > Storage
```

This creates a left-to-right arrow from `Compute` to `Storage`.

### Connector Types

- `>` : Left-to-right arrow
- `<` : Right-to-left arrow
- `<>`: Bi-directional arrow
- `-` : Plain line
- `--`: Dotted line
- `-->`: Dotted arrow

### Adding Labels to Connections

You can attach a label to a connection by appending a colon and the label text:

```plaintext
Storage > Server: Cache Hit
```

### One-to-Many Connections

Connect one node to several nodes in a single statement:

```plaintext
Server > Worker1, Worker2, Worker3
```

### Connection Properties

Similar to nodes, connections can have properties to customize their appearance. For example, to change the line color:

```plaintext
Storage > Server [color: green]
```

---

## Icons

Eraser.io supports a wide range of icons to represent various services and elements in your diagrams. Some key icon sets include:

- **AWS Icons** (e.g., `aws-ec2`, `aws-lambda`)
- **Google Cloud Icons** (e.g., `gcp-compute-engine`, `gcp-cloud-storage`)
- **Azure Icons** (e.g., `azure-virtual-machine`, `azure-sql-database`)
- **Tech Logos** and **General Icons**

For a full list of icon names, see the official documentation or the [Icons reference](https://docs.eraser.io/docs/syntax#icons).

---

## Escape String

Certain characters are reserved in node and group names. If you need to include such characters (or spaces), wrap the entire name in double quotes:

```plaintext
User > "https://localhost:8080": GET
```

---

## Direction

The overall direction of your diagram can be changed with the `direction` statement. Allowed directions include:

- `direction right` (default)
- `direction left`
- `direction down`
- `direction up`

You can place the direction statement anywhere in your code:

```plaintext
direction down
```

---

## Styling

Diagram-level styles can be applied using properties that affect the entire diagram. The main styling options are:

- **colorMode:** Sets the overall fill lightness (e.g., `pastel`, `bold`, `outline`)
- **styleMode:** Determines the style embellishments (e.g., `shadow`, `plain`, `watercolor`)
- **typeface:** Chooses the text typeface (e.g., `rough`, `clean`, `mono`)

Example usage:

```plaintext
colorMode bold
styleMode shadow
typeface clean
```

These settings help maintain a consistent look across your entire diagram.

---

This file provides a comprehensive overview of the syntax used to create diagrams with Eraser.io. By combining nodes, groups, properties, and connections, you can model complex architectures and workflows with clarity.
