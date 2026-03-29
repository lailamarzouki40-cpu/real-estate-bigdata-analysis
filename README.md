# 🏠 Real Estate Big Data Analysis Pipeline

🚀 A full end-to-end Big Data project that analyzes real estate markets using web scraping, data cleaning, Hadoop (HDFS), and MapReduce.

---

## 📌 Overview

This project builds a complete **data pipeline** to analyze real estate markets across multiple U.S. cities.
It covers the full lifecycle:

> **Scrape → Clean → Store → Process → Visualize**

The goal is to extract meaningful insights such as:

- 💰 Price per Bedroom (Affordability)
- 📏 Price per Square Foot (Value)

---

## 🧰 Tech Stack

- **Python** (Selenium, Regex, Pandas)
- **Web Scraping**: `undetected-chromedriver`, `Selenium`
- **Big Data**: Hadoop 3.2.1 (HDFS + MapReduce)
- **Containerization**: Docker
- **Visualization**: Matplotlib, Seaborn

---

## 🔄 Full Project Lifecycle

### 1. 🌐 Data Ingestion (Web Scraping)

Collected raw real estate data from:

- Zillow
- Realtor.com

**Approach:**

- Used Selenium with `undetected-chromedriver` to bypass bot detection
- Implemented **deep scrolling** to trigger lazy-loaded listings
- Handled CAPTCHA interruptions manually

**Cities Scraped:**

- Chicago
- Houston
- Dallas
- Phoenix

📁 Output:

```bash
realestate_raw.csv
```

---

### 2. 🧹 Data Cleaning (Regex Normalization)

Raw data was unstructured (e.g. `"3 bds | 2 ba | 1,500 sqft"`).

**Challenges:**

- Mixed text fields
- Missing structured columns
- Inconsistent formats

**Solution:**

- Used **Regular Expressions (Regex)** to:
  - Extract **Price** (remove `$`, `,`)
  - Extract **Beds** and **Square Footage**
  - Validate **Zip Codes** from address

📁 Output:

```bash
realestate_clean.csv
```

---

### 3. 🏗️ Infrastructure (Docker + Hadoop HDFS)

To simulate Big Data processing:

- Started a Hadoop cluster using Docker
- Created HDFS structure:

```bash
/project_realestate/clean/
```

- Uploaded cleaned dataset into HDFS:

```bash
hdfs dfs -put realestate_clean.csv /project_realestate/clean/
```

---

### 4. ⚙️ Distributed Processing (MapReduce)

Implemented 2 analytical MapReduce jobs:

---

#### 📊 Job #1: Market Affordability ($ / Bedroom)

**Goal:** Identify affordable housing areas.

- **Mapper Output:** `(ZipCode, [Price, Beds])`
- **Reducer Logic:**
  - Sum prices and beds
  - Compute average **price per bedroom**

---

#### 📈 Job #2: Value Analysis ($ / SqFt)

**Goal:** Evaluate property investment value.

- **Mapper Output:** `(ZipCode, [Price, SqFt])`
- **Reducer Logic:**
  - Aggregate total price and total square footage
  - Compute average **price per square foot**

---

### 5. 🐍 Technical Challenge (Python 3.5 Bug)

🚨 **Problem:**

- Hadoop container used an old Debian version
- Only supported **Python 3.5**
- My scripts used **f-strings (Python 3.6+)**

✅ **Solution:**

- Updated Debian sources to archive repositories
- Installed Python manually
- Refactored code:
  - Replaced f-strings with `.format()`

---

### 6. 📤 Data Extraction & Visualization

After processing:

**Extraction:**

```bash
hdfs dfs -get /output_folder
docker cp ...
```

**Visualization:**

- Bar charts (price per bedroom)
- Scatter plots (price vs sqft)
- Used **Matplotlib + Seaborn**

---

## 🔍 Key Insights

- 🏙️ **Houston shows extreme economic disparity**
  - Some ZIP codes: ~$100k per bedroom
  - Others: ~$3.5M per bedroom

👉 Conclusion:
**ZIP Code is a better analytical unit than City name**

---

## ✅ Final Result

✔️ Built a complete Big Data pipeline
✔️ Successfully processed distributed data using Hadoop
✔️ Generated meaningful real estate insights

---

## 🧠 What I Learned

- Managing data across:
  - Windows → Docker → HDFS

- Working with legacy systems (Python 3.5)
- Writing MapReduce jobs using Hadoop Streaming
- Handling real-world messy datasets
- Debugging distributed systems

---

## 🚀 Future Improvements

- Upgrade environment to Python 3.8+
- Automate pipeline (Airflow / scripts)
- Build a web dashboard (React / Flask)
- Add real-time data ingestion

---

## 📌 Conclusion

This project demonstrates a full **Big Data engineering workflow**, from raw web data collection to distributed analysis and visualization.

It highlights both:

- Technical implementation
- Real-world problem solving under constraints

---

## 👩‍💻 Author

**Laila Marzouki**
Big Data & Software Engineering Enthusiast 🚀
