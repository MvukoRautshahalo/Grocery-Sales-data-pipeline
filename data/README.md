# Data Source: Grocery Sales Dataset ()

## Overview

This directory contains the **raw source data** for the pipeline.
The dataset represents a **relational retail system** with multiple normalized tables covering customers, products, sales transactions, employees, and geographic hierarchy.

These files are treated as **immutable raw inputs** and should not be modified directly. All transformations must occur in the pipeline (`src/transform`).

---

## Data Structure

The dataset consists of **7 interconnected tables**:

| File             | Description                      |
| ---------------- | -------------------------------- |
| `categories.csv` | Product category definitions     |
| `cities.csv`     | City-level geographic data       |
| `countries.csv`  | Country metadata                 |
| `customers.csv`  | Customer demographic information |
| `employees.csv`  | Sales staff details              |
| `products.csv`   | Product catalog                  |
| `sales.csv`      | Transaction-level sales data     |

---

## Entity Relationships

This dataset follows a **normalized relational model**.

### Core Relationships:

* `sales` → links to:

  * `customers` (CustomerID)
  * `products` (ProductID)
  * `employees` (SalesPersonID)

* `products` → `categories` (CategoryID)

* `customers` → `cities` → `countries`

* `employees` → `cities` → `countries`

---

## Logical Schema (Simplified)

```
countries
   ↑
cities
   ↑
customers        employees
      \         /
        sales
          ↓
       products → categories
```

---

## Table Details

### 1. categories

Defines product groupings.

* Primary Key: `CategoryID`

---

### 2. cities

Geographic city-level data.

* Primary Key: `CityID`
* Foreign Key: `CountryID`

---

### 3. countries

Country reference table.

* Primary Key: `CountryID`

---

### 4. customers

Customer demographic and location data.

* Primary Key: `CustomerID`
* Foreign Key: `CityID`

---

### 5. employees

Sales personnel information.

* Primary Key: `EmployeeID`
* Foreign Key: `CityID`

---

### 6. products

Product catalog and attributes.

* Primary Key: `ProductID`
* Foreign Key: `CategoryID`

---

### 7. sales

Transactional fact table (core of the dataset).

* Primary Key: `SalesID`
* Foreign Keys:

  * `CustomerID`
  * `ProductID`
  * `SalesPersonID`

Contains:

* Quantity
* Discount
* TotalPrice
* SalesDate

---

## Data Engineering Notes

### 1. Grain

The **lowest level of granularity** is:

> One row per transaction (`sales` table)

---

### 2. Fact vs Dimension Mapping

| Type       | Tables                                                                    |
| ---------- | ------------------------------------------------------------------------- |
| Fact       | `sales`                                                                   |
| Dimensions | `customers`, `products`, `employees`, `categories`, `cities`, `countries` |

---

### 3. Pipeline Usage

In this project:

* `sales` → primary input for aggregation
* Dimensions → used for enrichment and joins

The pipeline will:

1. Ingest raw CSV files
2. Join relevant tables
3. Aggregate to **monthly-level features**
4. Load into PostgreSQL

---

### 4. Data Quality Considerations

Potential issues to handle in pipeline:

* Missing foreign key references
* Null or zero `TotalPrice`
* Inconsistent date formats in `SalesDate`
* Duplicate transaction records

---

## Important Rules

* Do NOT modify raw files
* Do NOT perform transformations in this folder
* Always treat this as **source-of-truth input**

---

## Next Step

See:

* `/src/ingest` → data loading
* `/src/transform` → business logic
* `/sql` → warehouse schema
