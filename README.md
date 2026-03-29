# Real Estate Big Data Analysis Pipeline

This project builds a complete data pipeline to analyze real estate markets using Hadoop and MapReduce.

It follows a simple workflow:

Scrape → Clean → Store → Process → Visualize

---

## Project Value

This project demonstrates how raw web data can be transformed into useful insights using a distributed system.

Instead of only analyzing data locally, it shows how to:

* Handle large and unstructured datasets
* Process data using Hadoop (HDFS + MapReduce)
* Extract meaningful insights for real estate decision-making

It reflects a real data engineering workflow from data collection to final analysis.

---

## Data Description

The raw data collected from real estate websites is unstructured and messy.

Example of raw data:

```text
"Property detail for Tract 2 Sheffield Rd Siloam Springs, AR ",
"$120,000",
"Property detail for Tract 2 Sheffield Rd Siloam Springs, AR 72761 Land for sale $120,000 2.38acre lot 2.38 acre lot Tract 2 Sheffield Rd Siloam Springs, AR 72761 Email Agent",
"Property detail for Tract 2 Sheffield Rd Siloam Springs, AR 72761 Land for sale $120,000 2.38acre lot 2.38 acre lot Tract 2 Sheffield Rd Siloam Springs, AR 72761 Email Agent",
"72761"
```

Problems with this data:

* Information is repeated
* Multiple values are mixed in one string
* Numbers are embedded in text
* Not directly usable for analysis

---
## Data Source

The dataset is based on publicly available real estate listings from major platforms such as Zillow and Realtor.com.

The data was collected for educational and analysis purposes only.

## Data Cleaning

To make the data usable, it was cleaned and structured using Python and Regular Expressions.

The cleaning process included:

* Extracting the price and converting it to a numeric value
* Extracting the number of bedrooms
* Extracting square footage
* Extracting ZIP codes from addresses
* Removing duplicated and unnecessary text

Example of cleaned data:

```text
"917 N Britt St Siloam Springs, AR 72761", 187000.0, 2.0, 830.0, 72761
```

Final structured columns:

* Address
* Price
* Bedrooms
* Square Footage
* Zip Code

This structured format makes the data ready for Hadoop processing.

---

## Processing (MapReduce)

Two MapReduce jobs were implemented:

### 1. Price per Bedroom (Affordability)

* Measures how much it costs to buy a bedroom in each ZIP code
* Useful for families looking for affordable housing

### 2. Price per Square Foot (Value)

* Measures property value based on space
* Useful for investors evaluating property worth

---

## Results Interpretation

```
==================================================
      REAL ESTATE BIG DATA MARKET REPORT
==================================================
```

### High-Value Areas (Expensive per Square Foot)

```
75229, 10010, 77024, 77027, 60654
```

These ZIP codes have very high price per square foot.
This means:

* Properties are expensive relative to their size
* These areas are likely premium or high-demand markets
* Investors pay more for location than space

---

### Affordable Areas (Best Price per Bedroom)

```
11301, 60621, 11637, 60628, 60636
```

These ZIP codes offer the lowest cost per bedroom.
This means:

* Better for families
* More rooms for less money
* Good residential affordability

---

### Undervalued Areas (Best Space for Price)

```
60628, 11301, 60621, 21426, 60636
```

These areas provide the most space for the lowest cost.
This means:

* Large properties at low prices
* Potential investment opportunities
* Often rural or less developed areas

---

### Key Insight

Some ZIP codes appear in both:

* affordable (low price per bedroom)
* undervalued (low price per sqft)

This indicates strong opportunities where:

* housing is cheap
* and space is large

Also, results show that:
**ZIP code is a better unit of analysis than city**,
because large cities can have very different markets inside them.

---

## Why Some Parts Are Not Included

* The full dataset is not included because it is large

* Only a sample is provided to show the structure

* The scraper code is not included because:

  * It depends on browser automation and CAPTCHA handling
  * It is not necessary to understand the data processing pipeline

This repository focuses on the **data engineering and analysis part**.

---

## Technologies Used

* Python
* Hadoop (HDFS + MapReduce)
* Docker
* Matplotlib / Seaborn

---

## Conclusion

This project shows how to transform raw, unstructured web data into structured insights using distributed processing.

It highlights:

* Data cleaning challenges
* Big Data processing with Hadoop
* Real-world analysis of real estate markets

---


##  Author

**Laila Marzouki**
Big Data & Software Engineering Enthusiast 🚀
