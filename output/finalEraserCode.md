Data_Processing_Analytics [icon: server, label: "Data Processing & Analytics"] {
  Data_Integration_Pipeline [icon: server, label: "Data Integration Pipeline\n(Custom Integration - Python)"]
  Advanced_Analytics_Automation [icon: server, label: "Advanced Analytics & Automation\n(Python)"]
}

User_Interface_Engagement [icon: globe, label: "User Interface & Engagement"] {
  Interactive_Web_Based_Dashboards [icon: globe, label: "Interactive Web-Based Dashboards\n(HTML5, JavaScript)"]
  Stakeholder_Engagement [icon: box, label: "Stakeholder Engagement"]
}

Cloud_Infrastructure [icon: aws-management-console, label: "Cloud Infrastructure"] {
  AWS_Cloud_Hosting_Compliance [icon: aws-management-console, label: "AWS Cloud Hosting & Compliance\n(AWS)"]
}

Geospatial_Analysis_Group [icon: globe, label: "Geospatial Analysis"] {
  Geospatial_Analysis [icon: globe, label: "Geospatial Analysis\n(ArcGIS)"]
}

AWS_Cloud_Hosting_Compliance > Data_Integration_Pipeline: Hosts the integration pipeline
AWS_Cloud_Hosting_Compliance > Advanced_Analytics_Automation: Provides hosting for advanced analytics
Data_Integration_Pipeline > Advanced_Analytics_Automation: Consolidated data flows into analytics
Advanced_Analytics_Automation > Interactive_Web_Based_Dashboards: Delivers processed analytics data to dashboards
Advanced_Analytics_Automation > Geospatial_Analysis: Sends analytical data for geospatial mapping
Geospatial_Analysis > Interactive_Web_Based_Dashboards: Integrates interactive maps into dashboards
Interactive_Web_Based_Dashboards > Stakeholder_Engagement: Delivers actionable insights to stakeholders