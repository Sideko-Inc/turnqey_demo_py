
# Turnqey Labs API Python SDK

## Overview
Turnqey is an API developer platform providing read-only, real-time data aggregation 
for performance reporting on held-away crypto assets.

### Synchronous Client

```python
from os import getenv
from turnqey_demo_py import Client

client = Client(
    token={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
```

### Asynchronous Client

```python
from os import getenv
from turnqey_demo_py import AsyncClient

client = AsyncClient(
    token={
        "client_id": getenv("OAUTH_CLIENT_ID"),
        "client_secret": getenv("OAUTH_CLIENT_SECRET"),
    }
)
```

## Module Documentation and Snippets

### [advisors](turnqey_demo_py/resources/advisors/README.md)

* [get](turnqey_demo_py/resources/advisors/README.md#get) - Get advisor by ID
* [list](turnqey_demo_py/resources/advisors/README.md#list) - Get financial advisors

### [auth](turnqey_demo_py/resources/auth/README.md)

* [create_token](turnqey_demo_py/resources/auth/README.md#create_token) - Generate access token using client ID and client secret

### [clients](turnqey_demo_py/resources/clients/README.md)

* [create](turnqey_demo_py/resources/clients/README.md#create) - Create a new client
* [delete](turnqey_demo_py/resources/clients/README.md#delete) - Delete client
* [get](turnqey_demo_py/resources/clients/README.md#get) - Get client by ID
* [list](turnqey_demo_py/resources/clients/README.md#list) - Get all clients
* [update](turnqey_demo_py/resources/clients/README.md#update) - Update client

### [clients.balances](turnqey_demo_py/resources/clients/balances/README.md)

* [get](turnqey_demo_py/resources/clients/balances/README.md#get) - Get client balances

### [clients.costbasis](turnqey_demo_py/resources/clients/costbasis/README.md)

* [get](turnqey_demo_py/resources/clients/costbasis/README.md#get) - Get cost basis information

### [clients.deposits_withdrawals](turnqey_demo_py/resources/clients/deposits_withdrawals/README.md)

* [get](turnqey_demo_py/resources/clients/deposits_withdrawals/README.md#get) - Get client deposits and withdrawals

### [clients.exchanges](turnqey_demo_py/resources/clients/exchanges/README.md)

* [create](turnqey_demo_py/resources/clients/exchanges/README.md#create) - Add exchange to client
* [get](turnqey_demo_py/resources/clients/exchanges/README.md#get) - Get client exchanges

### [clients.total_deposits_withdrawals](turnqey_demo_py/resources/clients/total_deposits_withdrawals/README.md)

* [get](turnqey_demo_py/resources/clients/total_deposits_withdrawals/README.md#get) - Get client total deposits and withdrawals

### [clients.trades](turnqey_demo_py/resources/clients/trades/README.md)

* [get](turnqey_demo_py/resources/clients/trades/README.md#get) - Get client trades

### [clients.transactions](turnqey_demo_py/resources/clients/transactions/README.md)

* [get](turnqey_demo_py/resources/clients/transactions/README.md#get) - Get client transactions

### [clients.transfers](turnqey_demo_py/resources/clients/transfers/README.md)

* [get](turnqey_demo_py/resources/clients/transfers/README.md#get) - Get client transfers

### [clients.wallets](turnqey_demo_py/resources/clients/wallets/README.md)

* [create](turnqey_demo_py/resources/clients/wallets/README.md#create) - Add wallet to client
* [delete](turnqey_demo_py/resources/clients/wallets/README.md#delete) - Remove wallet
* [get](turnqey_demo_py/resources/clients/wallets/README.md#get) - Get specific wallet
* [list](turnqey_demo_py/resources/clients/wallets/README.md#list) - Get client wallets

### [prices](turnqey_demo_py/resources/prices/README.md)

* [get](turnqey_demo_py/resources/prices/README.md#get) - Get current prices

### [prices.holding](turnqey_demo_py/resources/prices/holding/README.md)

* [get](turnqey_demo_py/resources/prices/holding/README.md#get) - Get holding prices

### [prices.settlement](turnqey_demo_py/resources/prices/settlement/README.md)

* [get](turnqey_demo_py/resources/prices/settlement/README.md#get) - Get settlement price

<!-- MODULE DOCS END -->
