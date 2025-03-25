
### create_token <a name="create_token"></a>
Generate access token using client ID and client secret

Authenticates with the provided credentials and returns an access token

**API Endpoint**: `POST /auth/token`

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
res = client.auth.create_token(
    client_id="c3f42b1a-1e4d-4b8f-9c5e-7d6a3b2c1e4f",
    client_secret="d7e8f9a0-b1c2-3d4e-5f6a-7b8c9d0e1f2a",
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
res = await client.auth.create_token(
    client_id="c3f42b1a-1e4d-4b8f-9c5e-7d6a3b2c1e4f",
    client_secret="d7e8f9a0-b1c2-3d4e-5f6a-7b8c9d0e1f2a",
)
```
