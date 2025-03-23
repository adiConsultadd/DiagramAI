# Eraser Diagram Examples

This document provides several complete examples to illustrate how Eraser.io’s diagram-as-code language can be used to create various types of diagrams, ranging from cloud architectures to workflows.

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

These examples illustrate a range of diagrams—from cloud architectures to workflows—using Eraser.io’s diagram-as-code language. You can adapt and expand these examples to suit your specific architecture and process needs.
