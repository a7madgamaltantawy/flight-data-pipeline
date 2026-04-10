

# ✈️ Flight Telemetry Data Pipeline (Azure Lakehouse)

## 📌 Overview

This project simulates a real-world data engineering scenario inspired by avionics and SCADA systems, where telemetry data is generated from multiple subsystems and needs to be ingested, validated, integrated, and transformed into meaningful insights.

The pipeline is designed using a **Lakehouse architecture on Azure**, leveraging **Databricks and ADLS** to process and manage large-scale telemetry data.

---

## 🎯 Objective

To design and implement an end-to-end data pipeline that:

* Ingests telemetry data from multiple subsystems
* Applies data validation rules to ensure data quality
* Integrates heterogeneous system data into a unified dataset
* Prepares structured data for downstream analytics and reporting

---

## 🛰️ Simulated Systems

The following subsystems are simulated:

* **Flight System** → altitude, speed, temperature
* **Battery System** → voltage, current, battery temperature
* **Control System** → flap position, engine thrust, yaw

These systems mimic real-world avionics telemetry sources.

---

## 🏗️ Architecture

![Image](https://images.openai.com/static-rsc-4/lIwpCmv_G-GhaZQ3MkJhIOsB4HP-5FIrQUoKmsH684lZZm1Djhu27GYPkRsivkfI7F3JPjLR_G-C5Ir7IrztybNgYmDO5bpR8g6BBXRwLAUpRR7hyk_mGC5nAz302mAb62lD5RDbRGdmW-kTrPPTs01w7hwOlAfE_pHYSV-6sD33xQmAd7qMbR3WfMyZBpx8?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/ehG0dcYLbtsClAztqI4QaXPcG41Qa8D1BpVcVsSChw0XX-aR0kfVd0EDsvZukLez0ob7l3LH_-qBAhYKEs0WWB4spuFL9aXYGzlEwYvMnCKtl9_vTvMpQ84tZPqNx1WcBcLlYUbXd2tETGnUjh_72wgYi_ZEN5cYaiyZ2_7h92IB58Thasg9kfSv_qa9wrpI?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/2FDO0F2Z4Y957G0RMtrRuKZmthPVY7jaqCpFlDExqNDoYPKCMn7DPO-NZstsO7ZvfPkgGvSYf5wPFMZuHg5AHLsUJQX9UkDFJ1IMPcQbVrNNmCwDWrvSJRVPuCFTydLduOuToFwnZOJTNiZK-aS-OXmT0XCGw38xjogtsJ47gh016Npcgviqf5LygZ9S1kZI?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/tIHW0JmmOvpSgIS513cZsZMiS7YDkcHiFzGjBJ6ePSX6pXxlO0O1RL5e7sZDqI4V_ZPE45mK9osSRTIAp5h9perqGSyRBZsJVihbys7rpbQOcI-19neD9ZN0IysXjbQhnKrEI---azpMXNcOAJ1TBkbf2YKQMAVP3VkcBW6DN7c5bdpouSqSK8WDEvtL3mLB?purpose=fullsize)

### Data Flow

1. **Raw Layer (Bronze)**

   * Raw CSV telemetry data is ingested into Azure Data Lake Storage.
   * No transformations applied.

2. **Validation Layer**

   * Engineering validation rules are applied to ensure data correctness.
   * Invalid records are filtered out.

3. **Integration Layer (Silver)**

   * Data from different subsystems is joined using:

     * `flight_id`
     * `timestamp`
   * Produces a unified telemetry dataset.

4. **Serving Layer (Gold)**

   * Aggregated and curated datasets for analytics (to be extended).

---

## ⚙️ Technology Stack

* **Azure Data Lake Storage (ADLS)** – Data storage
* **Azure Databricks** – Data processing (PySpark)
* **PySpark** – Transformations & validation
* **GitHub** – Version control & project showcase

---

## 🔄 Pipeline Stages

### 1. Bronze Ingestion

Raw telemetry files are ingested and stored in the bronze layer.

📂 Script: `01_ingest_bronze.py`

---

### 2. Flight Data Validation

Basic engineering rules are applied:

* Altitude must be > 0
* Speed must be > 0
* Temperature must not be null

📂 Script: `02_validate_flight_data.py`

---

### 3. System Integration (Silver Layer)

Validated flight data is joined with battery and control systems.

Join keys:

* `flight_id`
* `timestamp`

📂 Script: `03_integrate_systems_silver.py`

---

## 🧪 Data Quality Strategy

Data validation is treated as a first-class concern:

* Rule-based filtering
* Null checks
* Range validation

Future improvements:

* Anomaly detection
* Schema validation
* Data drift monitoring

---

## 🧠 Engineering Decisions

* **Lakehouse Architecture** → balances flexibility (data lake) with structure (warehouse)
* **Parquet Format** → optimized for performance and storage
* **Medallion Layers (Bronze/Silver/Gold)** → separation of concerns
* **Batch Processing** → sufficient for telemetry simulation (streaming can be added later)

---

## 📸 Screenshots

(See `/screenshots` folder)

---

## 🚀 Future Improvements

* Add Gold aggregation layer
* Implement streaming ingestion (Event Hubs)
* Add orchestration using Azure Data Factory
* Integrate dbt for transformation modeling
* Add dashboard (Power BI or similar)

---

## 👨‍💻 Author

Ahmed Tantawy
Data Engineer | Ex-Avionics Systems Engineer

