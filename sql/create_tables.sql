CREATE or replace TABLE feature_customer_monthly (
    customer_id INT,
    month DATE,

    total_spend NUMERIC,
    order_count INT,
    avg_order_value NUMERIC,
    total_units INT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (customer_id, month)
);