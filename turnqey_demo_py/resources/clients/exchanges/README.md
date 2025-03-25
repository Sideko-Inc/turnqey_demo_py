
### get <a name="get"></a>
Get client exchanges

Retrieve a list of exchanges for a specific client

**API Endpoint**: `GET /clients/{clientId}/exchanges`

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
res = client.clients.exchanges.get(client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
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
res = await client.clients.exchanges.get(
    client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)
```

### create <a name="create"></a>
Add exchange to client

Add a new exchange for a specific client

**API Endpoint**: `POST /clients/{clientId}/exchanges`

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
res = client.clients.exchanges.create(
    api_key="abc123def456ghi789",
    api_secret="secret123456789",
    client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    exchange_name="Coinbase",
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
res = await client.clients.exchanges.create(
    api_key="abc123def456ghi789",
    api_secret="secret123456789",
    client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    exchange_name="Coinbase",
)
```
