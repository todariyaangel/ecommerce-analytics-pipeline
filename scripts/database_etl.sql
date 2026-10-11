-- 1. Create Drop Table Statements for Clean Re-runs
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS users;

-- 2. Build Relational Schema Structure
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    signup_date TIMESTAMP,
    age INT,
    country VARCHAR(10),
    acquisition_channel VARCHAR(50)
);

CREATE TABLE events (
    event_id INT PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    event_type VARCHAR(50),
    timestamp TIMESTAMP
);

CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    order_value DECIMAL(10,2),
    transaction_date TIMESTAMP
);

-- 3. Production Analytics Portfolio Query (Funnel Performance)
-- Computes critical user tracking metrics from home landing to checkout completion
WITH funnel_stages AS (
    SELECT 
        user_id,
        COUNT(CASE WHEN event_type = 'home_page' THEN 1 END) as view_home,
        COUNT(CASE WHEN event_type = 'add_to_cart' THEN 1 END) as view_cart,
        COUNT(CASE WHEN event_type = 'purchase_success' THEN 1 END) as view_purchase
    FROM events
    GROUP BY user_id
)
SELECT 
    u.acquisition_channel,
    COUNT(DISTINCT f.user_id) as total_visitors,
    SUM(f.view_cart) as total_cart_adds,
    SUM(f.view_purchase) as total_purchases,
    ROUND((SUM(f.view_purchase)::NUMERIC / COUNT(DISTINCT f.user_id)::NUMERIC) * 100, 2) as overall_conversion_rate
FROM funnel_stages f
JOIN users u ON f.user_id = u.user_id
GROUP BY u.acquisition_channel
ORDER BY overall_conversion_rate DESC;
