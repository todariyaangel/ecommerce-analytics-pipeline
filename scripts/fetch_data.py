import pandas as pd
import numpy as np
import os

# Set seed for reproducibility
np.random.seed(42)
n_users = 1000

# 1. User Cohort Demographics
users = pd.DataFrame({
    'user_id': range(10001, 10001 + n_users),
    'signup_date': pd.date_range(start='2026-01-01', periods=n_users, freq='h'),
    'age': np.random.randint(18, 65, size=n_users),
    'country': np.random.choice(['US', 'UK', 'CA', 'DE', 'FR'], size=n_users, p=[0.5, 0.2, 0.1, 0.1, 0.1]),
    'acquisition_channel': np.random.choice(['Organic Search', 'Paid Ads', 'Email Marketing', 'Referral'], size=n_users)
})

# 2. Digital Marketing Conversion Funnel Logs
events = []
for uid in users['user_id']:
    stages = ['home_page', 'product_view', 'add_to_cart', 'checkout_page', 'purchase_success']
    max_stage = np.random.choice([1, 2, 3, 4, 5], p=[0.1, 0.2, 0.2, 0.1, 0.4])
    for idx, stage in enumerate(stages[:max_stage]):
        events.append({
            'event_id': len(events) + 1,
            'user_id': uid,
            'event_type': stage,
            'timestamp': pd.Timestamp('2026-02-01') + pd.Timedelta(days=np.random.randint(0, 28))
        })
events_df = pd.DataFrame(events)

# 3. Transaction Log Ledger
completed_purchases = events_df[events_df['event_type'] == 'purchase_success']
transactions = pd.DataFrame({
    'transaction_id': range(50001, 50001 + len(completed_purchases)),
    'user_id': completed_purchases['user_id'].values,
    'order_value': np.random.uniform(10.0, 300.0, size=len(completed_purchases)).round(2),
    'transaction_date': completed_purchases['timestamp'].values
})

# Export Data Pipelines to Target Directories
os.makedirs('data/raw', exist_ok=True)
users.to_csv('data/raw/users.csv', index=False)
events_df.to_csv('data/raw/events.csv', index=False)
transactions.to_csv('data/raw/transactions.csv', index=False)

print("Data Ingestion Pipeline Complete. Source CSV files written to data/raw/")
