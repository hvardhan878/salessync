# In-memory "database" for users and Salesforce data

from typing import Dict, List

# Users: username -> user dict
users: Dict[str, dict] = {
    "demo": {"username": "demo", "password": "password", "full_name": "Demo User"}
}

# Salesforce Accounts: list of dicts
accounts: List[dict] = [
    {"id": "001", "name": "Acme Corp", "industry": "Manufacturing"},
    {"id": "002", "name": "Globex Inc", "industry": "Technology"},
]

# Salesforce Opportunities: list of dicts
opportunities: List[dict] = [
    {"id": "op1", "name": "Big Deal", "stage": "Prospecting", "amount": 100000.0},
    {"id": "op2", "name": "Renewal", "stage": "Closed Won", "amount": 50000.0},
]