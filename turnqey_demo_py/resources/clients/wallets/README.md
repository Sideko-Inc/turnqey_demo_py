
### delete <a name="delete"></a>
Remove wallet

Remove a wallet from a client

**API Endpoint**: `DELETE /clients/{clientId}/wallets/{walletId}`

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
res = client.clients.wallets.delete(
    client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", wallet_id="string"
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
res = await client.clients.wallets.delete(
    client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", wallet_id="string"
)
```

### list <a name="list"></a>
Get client wallets

Retrieve a list of wallets for a specific client

**API Endpoint**: `GET /clients/{clientId}/wallets`

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
res = client.clients.wallets.list(client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
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
res = await client.clients.wallets.list(
    client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)
```

### get <a name="get"></a>
Get specific wallet

Retrieve a specific wallet for a client

**API Endpoint**: `GET /clients/{clientId}/wallets/{walletId}`

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
res = client.clients.wallets.get(
    client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", wallet_id="string"
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
res = await client.clients.wallets.get(
    client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a", wallet_id="string"
)
```

### create <a name="create"></a>
Add wallet to client

Add a new wallet for a specific client

**API Endpoint**: `POST /clients/{clientId}/wallets`

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
res = client.clients.wallets.create(
    address="0x71C7656EC7ab88b098defB751B7401B5f6d8976F",
    blockchain="Ethereum",
    client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    label="Main ETH Wallet",
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
res = await client.clients.wallets.create(
    address="0x71C7656EC7ab88b098defB751B7401B5f6d8976F",
    blockchain="Ethereum",
    client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    label="Main ETH Wallet",
)
```
