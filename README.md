# datadog-api-client-python

This repository contains a Python API client for the [Datadog API](https://docs.datadoghq.com/api/).

## Requirements

Building and using the API client library requires [Python 3.7+](https://www.python.org/downloads/).

## Installation

To install the API client library, simply execute:

```shell
pip install datadog-api-client
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Python code:

```python
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from datadog_api_client.v1.model.monitor import Monitor
from datadog_api_client.v1.model.monitor_type import MonitorType

body = Monitor(
    name="example",
    type=MonitorType("log alert"),
    query='logs("service:foo AND type:error").index("main").rollup("count").by("source").last("5m") > 2',
    message="some message Notify: @hipchat-channel",
    tags=["test:example", "env:ci"],
    priority=3,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.create_monitor(body=body)
    print(response)
```

### Authentication

By default the library will use the `DD_API_KEY` and `DD_APP_KEY` environment variables to authenticate against the Datadog API.
To provide your own set of credentials, you need to set some keys on the configuration:

```python
configuration.api_key["apiKeyAuth"] = "<API KEY>"
configuration.api_key["appKeyAuth"] = "<APPLICATION KEY>"
```

### Unstable Endpoints

This client includes access to Datadog API endpoints while they are in an unstable state and may undergo breaking changes. An extra configuration step is required to enable these endpoints:

```python
configuration.unstable_operations["<OperationName>"] = True
```

where `<OperationName>` is the name of the method used to interact with that endpoint. For example: `list_log_indexes`, or `get_logs_index`

### Changing Server

When talking to a different server, like the `eu` instance, change the `server_variables` on your configuration object:

```python
configuration.server_variables["site"] = "datadoghq.eu"
```

### Disable compressed payloads

If you want to disable GZIP compressed responses, set the `compress` flag
on your configuration object:

```python
configuration.compress = False
```

### Enable requests logging

If you want to enable requests logging, set the `debug` flag on your configuration object:

```python
configuration.debug = True
```

### Enable retry

If you want to enable retry when getting status code `429` rate-limited, set `enable_retry` to `True`

```python
    configuration.enable_retry = True
```

The default max retry is `3`, you can change it with `max_retries`

```python
    configuration.max_retries = 5
```

### Configure proxy

You can configure the client to use proxy by setting the `proxy` key on configuration object:

```python
configuration.proxy = "http://127.0.0.1:80"
```

### Threads support

You can run API calls in a thread by using `ThreadedApiClient` in place of `ApiClient`. API calls will then
return a `AsyncResult` instance on which you can call get to retrieve the result:

```python
from datadog_api_client import Configuration, ThreadedApiClient
from datadog_api_client.v1.api.dashboards_api import DashboardsApi

configuration = Configuration()
with ThreadedApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    result = api_instance.list_dashboards()
    dashboards = result.get()
    print(dashboards)
```

### Asyncio support

The library supports asynchronous operations when using `AsyncApiClient` for the transport. When that client is used,
the API methods will then return coroutines that you can wait for.

To make async support available, you need to install the extra `async` qualifiers during installation: `pip install datadog-api-client[async]`.

```python
import asyncio

from datadog_api_client import Configuration, AsyncApiClient
from datadog_api_client.v1.api.dashboards_api import DashboardsApi

async def main():
    configuration = Configuration()
    async with AsyncApiClient(configuration) as api_client:
        api_instance = DashboardsApi(api_client)
        dashboards = await api_instance.list_dashboards()
        print(dashboards)

asyncio.run(main())
```

### Pagination

Several listing operations have a pagination method to help consume all the items available.
For example, to retrieve all your incidents:

```python
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

configuration = Configuration()
configuration.unstable_operations["list_incidents"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    for incident in api_instance.list_incidents_with_pagination():
        print(incident.id)
```

## Documentation for API Endpoints and Models

Documentation for API endpoints and models are available on [readthedocs](https://datadog-api-client.readthedocs.io/).

## Documentation for Authorization

Authenticate with the API by providing your API and Application keys in the configuration:

```python
configuration.api_key["apiKeyAuth"] = "YOUR_API_KEY"
configuration.api_key["appKeyAuth"] = "YOUR_APPLICATION_KEY"
```

## Author

support@datadoghq.com
