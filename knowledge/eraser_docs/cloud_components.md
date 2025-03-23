# Cloud Components

This document focuses on representing cloud architectures using Eraser.io’s diagram-as-code language. It explains how to model compute resources, storage services, databases, and other cloud components using nodes, groups, and properties.

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

This level of customization helps maintain clarity in complex diagrams, ensuring each component’s role is easily identifiable.

---

This file serves as a guide to modeling cloud architectures with Eraser.io. By combining nodes, groups, and properties, you can create detailed and visually appealing diagrams that accurately reflect your cloud infrastructure.
