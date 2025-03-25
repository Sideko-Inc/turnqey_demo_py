
### get <a name="get"></a>
Get client deposits and withdrawals

Retrieve deposit and withdrawal information for a client

**API Endpoint**: `GET /clients/{clientId}/deposits-withdrawals`

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
res = client.clients.deposits_withdrawals.get(
    client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)
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
res = await client.clients.deposits_withdrawals.get(
    client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)
```
