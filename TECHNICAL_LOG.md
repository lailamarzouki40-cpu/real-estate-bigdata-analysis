# Technical Log – Hadoop Real Estate Project

This document records the technical execution steps performed to build and run the Hadoop-based Real Estate analysis pipeline.

---

## 1. Starting the Cluster

The Hadoop environment was initialized from the Windows terminal within the project folder.

```bash
cd C:\Users\hp\Desktop\Realestate-project
docker-compose up -d

# Create the folder inside the container for MapReduce scripts
docker exec namenode mkdir -p /mapreduce_re
```

---

## 2. Setting up HDFS & Moving Data

Since `docker cp` only works from the Windows host, the cleaned dataset was first copied into the container’s temporary storage before being uploaded to HDFS.

```bash
# From Windows (Host)
docker cp data/realestate_clean.csv namenode:/tmp/realestate_clean.csv
```

Then, inside the container:

```bash
docker exec -it namenode bash

# Create HDFS directory structure
hdfs dfs -mkdir -p /project_realestate/clean
hdfs dfs -mkdir -p /project_realestate/output_affordability
hdfs dfs -mkdir -p /project_realestate/output_value

# Upload dataset to HDFS
hdfs dfs -put /tmp/realestate_clean.csv /project_realestate/clean/

# Verify upload
hdfs dfs -ls -R /project_realestate

exit
```

---

## 3. Uploading MapReduce Scripts

The MapReduce Python scripts were uploaded from the Windows host to the container.

```bash
# From Windows (Host)
docker cp mapreduce/mapper_affordability.py namenode:/mapreduce_re/
docker cp mapreduce/reducer_affordability.py namenode:/mapreduce_re/
docker cp mapreduce/mapper_value.py namenode:/mapreduce_re/
docker cp mapreduce/reducer_value.py namenode:/mapreduce_re/
```

---

## 4. Running MapReduce Job #1 (Market Affordability)

Executed the first job to compute price per bedroom.

```bash
docker exec -it namenode bash
cd /mapreduce_re

# Run Hadoop Streaming job
hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
  -input /project_realestate/clean/realestate_clean.csv \
  -output /project_realestate/output_affordability/run1 \
  -mapper "python3 mapper_affordability.py" \
  -reducer "python3 reducer_affordability.py" \
  -file mapper_affordability.py \
  -file reducer_affordability.py

exit
```

---

## 5. Running MapReduce Job #2 (Value Analysis)

Executed the second job to compute price per square foot.

```bash
docker exec -it namenode bash
cd /mapreduce_re

# Run Hadoop Streaming job
hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
  -input /project_realestate/clean/realestate_clean.csv \
  -output /project_realestate/output_value/run1 \
  -mapper "python3 mapper_value.py" \
  -reducer "python3 reducer_value.py" \
  -file mapper_value.py \
  -file reducer_value.py

# Display results
hdfs dfs -cat /project_realestate/output_value/run1/part-00000
```

---

## Summary

- Hadoop cluster successfully deployed using Docker
- Data uploaded and organized in HDFS
- MapReduce scripts executed using Hadoop Streaming
- Two analyses completed:
  - Price per bedroom (affordability)
  - Price per square foot (value)

This confirms a complete and functional distributed data processing workflow.
