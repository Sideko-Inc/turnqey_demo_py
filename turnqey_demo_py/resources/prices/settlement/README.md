
### get <a name="get"></a>
Get settlement price

Retrieve settlement price for an asset

**API Endpoint**: `GET /settlement-price`

#### Synchronous Client

```python
from os import getenv
from turnqey_demo_py import Client

client = Client(
    token={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = client.prices.settlement.get(date="1970-01-01", symbol_field="string")
```

#### Asynchronous Client

```python
from os import getenv
from turnqey_demo_py import AsyncClient

client = AsyncClient(
    token={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
res = await client.prices.settlement.get(date="1970-01-01", symbol_field="string")
```
