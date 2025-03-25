
### delete <a name="delete"></a>
Delete client

Delete a client by ID

**API Endpoint**: `DELETE /clients/{clientId}`

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
res = client.clients.delete(client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
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
res = await client.clients.delete(client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
```

### list <a name="list"></a>
Get all clients

Retrieve a list of all clients

**API Endpoint**: `GET /clients`

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
res = client.clients.list()
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
res = await client.clients.list()
```

### get <a name="get"></a>
Get client by ID

Retrieve a specific client by ID

**API Endpoint**: `GET /clients/{clientId}`

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
res = client.clients.get(client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
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
res = await client.clients.get(client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
```

### create <a name="create"></a>
Create a new client

Create a new client in the system

**API Endpoint**: `POST /clients`

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
res = client.clients.create(
    email_field="john.doe@example.com", name="John Doe", phone="+1-555-123-4567"
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
res = await client.clients.create(
    email_field="john.doe@example.com", name="John Doe", phone="+1-555-123-4567"
)
```

### update <a name="update"></a>
Update client

Update an existing client

**API Endpoint**: `PUT /clients/{clientId}`

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
res = client.clients.update(
    client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    email_field="john.doe@example.com",
    name="John Doe",
    phone="+1-555-123-4567",
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
res = await client.clients.update(
    client_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    email_field="john.doe@example.com",
    name="John Doe",
    phone="+1-555-123-4567",
)
```
