ecommerce-data-pipeline/
│
├── config/
│   └── config.yaml
│
├── data/
│   └── raw/   # (optional if using DBFS paths)
│
├── notebooks/
│   └── 01_explore_data.py
│
├── src/
│   ├── ingest/
│   │   └── ingest_data.py
│   │
│   ├── transform/
│   │   └── transform_sales.py
│   │
│   ├── load/
│   │   └── load_postgres.py
│   │
│   ├── utils/
│   │   ├── db.py
│   │   └── logger.py
│   │
│   └── main.py
│
├── sql/
│   └── create_tables.sql
│
├── requirements.txt
└── README.md