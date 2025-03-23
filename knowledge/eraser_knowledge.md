# Cloud Components

This document focuses on representing cloud architectures using Eraser.io's diagram-as-code language. It explains how to model compute resources, storage services, databases, and other cloud components using nodes, groups, and properties.

---

## Defining Cloud Nodes

Cloud nodes represent individual services or components in your architecture. Each node is defined by a unique name and can include properties such as an icon or color. For example:

```plaintext
compute [icon: aws-ec2]
storage [icon: aws-simple-storage-service, color: "#f0f0f0"]
database [icon: aws-rds, label: "RDS Database"]
```

_Key Points:_

- Use cloud-specific icons (e.g., `aws-ec2`, `gcp-compute-engine`, `azure-virtual-machine`) to visually represent services.
- Optionally use properties to customize the appearance of each node.

---

## Grouping Cloud Components

Grouping allows you to encapsulate related nodes into a logical container. This is useful for representing components such as Virtual Private Clouds (VPCs), subnets, or tiers (e.g., public and private subnets).

### Example: Grouping by Subnet

```plaintext
VPC {
  Public_Subnet {
    WebServer [icon: aws-ec2]
    LoadBalancer [icon: aws-elastic-load-balancer]
  }
  Private_Subnet {
    AppServer [icon: aws-ec2]
    Database [icon: aws-rds]
  }
}
```

_Notes:_

- Group names must be unique.
- Groups can be nested to reflect hierarchical architectures.

---

## Cloud Service Icons

Eraser.io includes a variety of icons for popular cloud providers. Some examples include:

- **AWS:**

  - `aws-ec2` for compute instances
  - `aws-lambda` for serverless functions
  - `aws-rds` for relational databases

- **Google Cloud:**

  - `gcp-compute-engine` for virtual machines
  - `gcp-cloud-storage` for object storage
  - `gcp-pubsub` for messaging services

- **Azure:**
  - `azure-virtual-machine` for compute instances
  - `azure-sql-database` for database services
  - `azure-load-balancers` for load balancing

For a complete list of available icons, please refer to the [Icons reference](https://docs.eraser.io/docs/syntax#icons).

---

## Example Cloud Architecture

Below is an example snippet that models a simple cloud architecture using a combination of nodes and groups:

```plaintext
API_Gateway [icon: aws-api-gateway]
Lambda [icon: aws-lambda]
S3 [icon: aws-simple-storage-service]

VPC {
  Public_Subnet {
    Server [icon: aws-ec2]
    Data [icon: aws-rds]
  }
  Queue [icon: aws-auto-scaling]
}

Analytics [icon: aws-redshift]

// Define connections to represent data flow
API_Gateway > Lambda > Server > Data
Server > Queue
S3 < Data
```

_Explanation:_

- **Nodes:** Represent individual cloud services.
- **Groups:** `VPC` groups together subnets like `Public_Subnet` which contains both a server and a database.
- **Connections:** Illustrate how data or processes flow between the components.

---

## Customizing Cloud Components

You can further customize each node and group using properties:

- **color:** Change the color for visual differentiation.
- **label:** Override the default node name to provide a more descriptive label.
- **Other styling properties:** Use `colorMode`, `styleMode`, and `typeface` for consistent aesthetics across your diagram.

For example:

```plaintext
WebServer [icon: aws-ec2, color: blue, label: "Web Server", typeface: clean]
```

This level of customization helps maintain clarity in complex diagrams, ensuring each component's role is easily identifiable.

---

This file serves as a guide to modeling cloud architectures with Eraser.io. By combining nodes, groups, and properties, you can create detailed and visually appealing diagrams that accurately reflect your cloud infrastructure.

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

Like nodes and groups, connections can be styled with properties. Properties are added at the end of the connection statement within square brackets. For example, to set the connection's line color to green, use:

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

# Eraser Diagram Examples

This document provides several complete examples to illustrate how Eraser.io's diagram-as-code language can be used to create various types of diagrams, ranging from cloud architectures to workflows.

---

## AWS Diagram Example

This example models a simple AWS cloud architecture:

```plaintext
// Define groups and nodes
API_Gateway [icon: aws-api-gateway]
Lambda [icon: aws-lambda]
S3 [icon: aws-simple-storage-service]

VPC {
  Public_Subnet {
    Server [icon: aws-ec2]
    Data [icon: aws-rds]
  }
  Queue [icon: aws-auto-scaling]
}

Analytics [icon: aws-redshift]

// Define connections
API_Gateway > Lambda > Server > Data
Server > Queue
S3 < Data
```

_Explanation:_

- Nodes like `API_Gateway`, `Lambda`, and `S3` represent individual AWS services.
- The `VPC` group contains sub-groups for public resources and a queue node.
- Connections show the flow of data and service interactions.

---

## Google Cloud Diagram Example

This example demonstrates a Google Cloud architecture:

```plaintext
// Define groups and nodes
Stream [icon: kafka, color: grey]
Ingest {
  Pub_Sub [icon: gcp-pubsub]
  Logging [icon: gcp-cloud-logging]
}
Pipelines {
  Dataflow [icon: gcp-dataflow]
}
Storage [icon: gcp-cloud-storage] {
  Datastore [icon: gcp-datastore]
  Bigtable [icon: gcp-bigtable]
}
Analytics {
  BigQuery [icon: gcp-bigquery]
}
Application [icon: gcp-app-engine] {
  App_Engine [icon: gcp-app-engine]
  Container_Engine [icon: gcp-container-registry]
  Compute_Engine [icon: gcp-compute-engine]
}

// Define connections
Stream > Ingest
Logging > Analytics > Application
Pub_Sub > Pipelines > Storage > Application
```

_Explanation:_

- This diagram breaks down the system into stages like ingestion, processing, storage, and application layers.
- Each group encapsulates related services, and the connections depict data flow between them.

---

## Azure Diagram Example

This example illustrates a simple architecture on Microsoft Azure:

```plaintext
// Define groups and nodes
AD_Tenant [icon: azure-active-directory]
Load_Balancers [icon: azure-load-balancers]

Virtual_Network {
  Web_Tier {
    VM1 [icon: azure-virtual-machine]
    VM2 [icon: azure-virtual-machine]
    VM3 [icon: azure-virtual-machine]
  }
  Business_Tier {
    LB2 [icon: azure-load-balancers]
    VM4 [icon: azure-virtual-machine]
    VM5 [icon: azure-virtual-machine]
    VM6 [icon: azure-virtual-machine]
  }
}

// Define connections
AD_Tenant > Load_Balancers
Load_Balancers > VM1, VM2, VM3
VM1, VM2, VM3 > LB2 > VM4, VM5, VM6
```

_Explanation:_

- The `Virtual_Network` groups resources into tiers.
- Connections clearly outline the relationship between Active Directory, load balancers, and virtual machines.

---

## Kubernetes Diagram Example

This example shows how to represent a Kubernetes cluster:

```plaintext
// Define groups and nodes
Cloud_Provider_API [icon: settings]
AWS [icon: aws]
GCP [icon: google-cloud]
Azure [icon: azure]

Control_Plane [icon: k8s-control-plane] {
  API [icon: k8s-api]
  Scheduler [icon: k8s-sched]
  etcd [icon: k8s-etcd]
}

Node1 [icon: k8s-node] {
  Kubelet1 [icon: k8s-kubelet]
  KProxy1 [icon: k8s-k-proxy]
}
Node2 [icon: k8s-node] {
  Kubelet2 [icon: k8s-kubelet]
  KProxy2 [icon: k8s-k-proxy]
}
Node3 [icon: k8s-node] {
  Kubelet3 [icon: k8s-kubelet]
  KProxy3 [icon: k8s-k-proxy]
}

// Define connections
Control_Plane > API, Scheduler, etcd
Kubelet1, KProxy1, Kubelet2, KProxy2, Kubelet3, KProxy3 > API
```

_Explanation:_

- The control plane and worker nodes are distinctly grouped.
- Connections indicate how worker nodes interact with the API server.

---

## Data ETL Pipeline Example

This example models a data ETL (Extract, Transform, Load) pipeline:

```plaintext
// Define groups and nodes
Input_Data_Sources {
  Oracle [icon: oracle]
  Twitter [icon: twitter]
  Facebook [icon: facebook]
}

ETL_Pipeline [color: silver] {
  Survey_Data [icon: kafka]
  Data_Load [icon: aws-s3]
  Data_Transformation [icon: databricks]
  Data_Store [icon: snowflake]
}

Data_Destinations {
  Notification [icon: slack]
  Experimentation [icon: tensorflow]
  BI_Dashboard [icon: tableau]
}

// Define connections
Oracle, Twitter, Facebook > Survey_Data
Survey_Data > Data_Load > Data_Transformation > Data_Store
Data_Store > Notification, Experimentation, BI_Dashboard
```

_Explanation:_

- This diagram shows a typical ETL flow from data sources through processing stages to various destinations.
- Grouping helps distinguish between input sources, the pipeline, and output targets.

---

## Doctor Onboarding Workflow Example

A workflow example for onboarding doctors into an appointment scheduling app:

```plaintext
Fetch_Locations [icon: map-marker]
Check_Location_Count [icon: checklist]
Add_to_Salesforce [icon: cloud-upload]
Video_Call [icon: video-camera]
WY_Questionnaire [icon: form]
Finish_Onboarding [icon: check]

Fetch_Locations > Check_Location_Count
Check_Location_Count > Add_to_Salesforce: If > 4 locations
Check_Location_Count > Video_Call
Video_Call > WY_Questionnaire: If authorized in Wyoming
Video_Call > Finish_Onboarding: Otherwise, complete onboarding
```

_Explanation:_

- Each node represents a step in the onboarding process.
- Conditional labels on the connections explain decision points and branching logic.

---

These examples illustrate a range of diagrams—from cloud architectures to workflows—using Eraser.io's diagram-as-code language. You can adapt and expand these examples to suit your specific architecture and process needs.

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
# Workflow Diagrams

Workflow diagrams are used to depict processes, sequential steps, and decision points within a system. With Eraser.io's diagram-as-code language, you can create clear and structured representations of workflows.

---

## Defining Workflow Steps

Each step in a workflow is represented by a node. You can assign icons, colors, and labels to clarify the purpose of each step. For example:

```plaintext
Start [icon: play]
Process [icon: gears]
Decision [icon: question]
End [icon: stop]
```

_Note:_

- Use descriptive node names and icons that best represent the step.
- Customize appearance with properties like `color` and `label` when needed.

---

## Grouping Workflow Stages

For processes that include multiple stages or sub-processes, group related nodes together. This helps to visualize parts of the process that belong to the same phase. For example:

```plaintext
User_Onboarding {
  Registration [icon: user-plus]
  Verification [icon: check-circle]
  Welcome [icon: smile]
}
```

_Key Points:_

- Group names must be unique.
- Grouping creates a visual boundary that clarifies the flow within a larger process.

---

## Sequential Flow

Indicate the order of operations using connection arrows. The simplest sequential workflow uses a series of nodes connected by arrows:

```plaintext
Start > Registration > Verification > Welcome > End
```

_Tip:_

- Ensure the connections clearly represent the flow of the process.

---

## Conditional Paths and Branching

Workflows often involve decisions that lead to different outcomes. Represent these scenarios by connecting a single node to multiple outcome nodes, and add labels to clarify the conditions:

```plaintext
Decision > Approved, Rejected
```

Or with labels specifying conditions:

```plaintext
Decision > Approved: If valid credentials, Rejected: If invalid
```

_Key Consideration:_

- Use labels to help stakeholders quickly understand the branching logic in the workflow.

---

## Example: Doctor Onboarding Flow

Below is an example workflow that shows how to onboard doctors to an appointment scheduling application:

```plaintext
Fetch_Locations [icon: map-marker]
Check_Location_Count [icon: checklist]
Add_to_Salesforce [icon: cloud-upload]
Video_Call [icon: video-camera]
WY_Questionnaire [icon: form]
Finish_Onboarding [icon: check]

Fetch_Locations > Check_Location_Count
Check_Location_Count > Add_to_Salesforce: If > 4 locations
Check_Location_Count > Video_Call
Video_Call > WY_Questionnaire: If authorized in Wyoming
Video_Call > Finish_Onboarding: Otherwise, complete onboarding
```

_Explanation:_

- **Fetch_Locations:** Initiates the process by gathering practice location data.
- **Check_Location_Count:** Determines if the number of locations requires additional steps.
- **Add_to_Salesforce:** Integrates with Salesforce if there are more than 4 locations.
- **Video_Call:** Continues with a video call step for further verification.
- **WY_Questionnaire:** Displays a special questionnaire for doctors authorized in Wyoming.
- **Finish_Onboarding:** Concludes the onboarding process when conditions are met.

---

This file provides guidance on modeling workflows with Eraser.io. By combining nodes, groups, connections, and conditional labels, you can effectively represent processes, branching decisions, and sequential steps in your system diagrams.
