# 🔢 Distributed K-Means Clustering Using MapReduce & gRPC  
A fully distributed, fault-tolerant implementation of the **K-Means clustering algorithm** using a custom **MapReduce pipeline** coordinated through **gRPC communication**. This system processes large datasets by splitting work across multiple Mappers and Reducers, ensuring scalability, parallelism, and iterative centroid refinement.

---

## 📌 Overview  
This architecture supports:

- Parallel K-Means clustering using MapReduce  
- Iterative centroid updates  
- Fully asynchronous gRPC-based communication  
- Automatic fault handling and task re-execution  
- Distributed processing of large point datasets  

![Alt text](../../images/mapreduce_flow.jpg)

---

## 🧱 System Components

---

### 🔷 1. **Master Component**

The **central orchestrator** for the entire K-Means workflow.

#### **Responsibilities**
- Accepts system configuration parameters:
  - `M` → number of Mappers  
  - `R` → number of Reducers  
  - `K` → number of centroids  
  - number of iterations  
- Splits the input dataset (`points.txt`) into **input splits** for mappers.  
- Sends tasks, centroids, and metadata to Mappers and Reducers.  
- Collects reducer outputs to compile new centroids after each iteration.  

#### **Iteration Workflow**
1. Split input → dispatch to Mappers  
2. Collect mapper partitions  
3. Trigger Reducers  
4. Compile updated centroids  
5. Repeat until iterations complete  

---

### 🔷 2. **Mapper Component**

Each Mapper independently processes a subset of data assigned by the Master.

#### **Execution Steps**
- Reads its assigned input split.  
- Loads the current centroid list provided by the Master.  
- For each data point:
  - Computes its nearest centroid.  
  - Emits:
    ```
    Key: Centroid Index  
    Value: Data Point  
    ```

#### **Output**
Intermediate data is stored as partition files in:
- Mappers/M1/
- Mappers/M2/

---

### 🔷 3. **Partition Function**

Ensures that intermediate data is grouped correctly before reduction.

#### **Mechanism**
- Uses a partitioning rule such as:
`partition_index = centroid_index % R`
- Guarantees:
- All points for the same centroid → same Reducer  
- Balanced reducer workload  

Partitioned outputs are stored inside each Mapper’s directory.

---

### 🔷 4. **Reducer Component**

Reducers process intermediate Mapper outputs and compute updated centroids.

#### **Key Responsibilities**
- Fetch partition files from all mappers (**shuffle phase**).  
- Sort & group by centroid index (**sort phase**).  
- For each centroid:
- Gather all assigned data points.  
- Compute the **mean vector** → new centroid.

#### **Output**
Reducers emit:
- ``Key: Centroid ID``
- ``Value: Updated Centroid``

Saved as:
- Reducers/R1.txt
- Reducers/R2.txt

---

## 🔄 Master’s Centroid Compilation

Once all reducers finish:

1. Master reads every reducer’s output file.  
2. Collects & merges updated centroids.  
3. Generates the global centroid list for the next iteration.  
4. Sends this centroid list to all mappers for the next iteration.  

This loop repeats until the desired number of iterations is complete.

---

## 📡 gRPC Communication Overview

### 🟦 **Master → Mapper**
- Sends input splits  
- Sends centroid list  
- Invokes map & partition tasks  

### 🟥 **Master → Reducer**
- Signals start of reduce phase  
- Provides necessary partition metadata  

### 🟩 **Reducer → Mapper**
- Reducers request partition files for each centroid group  
- Required for performing the shuffle stage  

### 🟨 **Master → Reducer (Final Phase)**
- Fetches reducer outputs  
- Builds the updated centroid list  

---

## 🛡 Fault Tolerance

The system ensures reliability even during node or task failures.

### ✔ Failure Handling
- If a Mapper or Reducer reports: "failed" or "unsuccessful"
→ Master automatically **reruns** the task.

- If the worker node fails repeatedly:
→ Master **reassigns** the task to a new Mapper or Reducer.

### ✔ Guarantees
- No data loss  
- Safe re-execution due to deterministic operations  
- High resiliency in distributed environments  

---

## 📈 Advantages of This Architecture

- **Highly parallelized** data processing using MapReduce  
- **Scalable** to large datasets and high computation loads  
- **Efficient** communication via gRPC  
- **Fault-tolerant** execution  
- **Iterative refinement** ideal for K-Means  
- **Structured shuffle & sort** enables deterministic results  
- **Decoupled design** allows independent scaling of Mappers and Reducers  

---

## 🧭 Summary

This distributed K-Means clustering system integrates:

- MapReduce-style computation  
- gRPC-based inter-process communication  
- Robust fault-tolerant mechanisms  
- Iterative convergence through updated centroid lists  

It is ideal for educational, experimental, or production-grade distributed machine learning scenarios involving large-scale clustering.

---


