# datadog-api-client-python

This library allows you to quickly and easily use the [Datadog API](https://docs.datadoghq.com/api/) v1 and v2 with Python.

The code is automatically generated using [openapi-generator](https://github.com/OpenAPITools/openapi-generator)
and [apigentools](https://github.com/DataDog/apigentools).

## Requirements

Building and using the API client library requires [Python 3.6+](https://www.python.org/downloads/).

To use the Datadog API, you need Datadog [API](https://app.datadoghq.com/account/settings#api) and [Application keys](https://app.datadoghq.com/access/application-keys).

## Install Package

```shell
pip install datadog-api-client
```

## Authentication

After [installing the Python package](#install-package), execute the following code to authenticate to the Datadog API:

```python
import os
from dateutil.parser import parse as dateutil_parser
import datadog_api_client.v1
from datadog_api_client.v1.api import aws_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint

# Defining the host is optional and defaults to https://api.datadoghq.com
# See configuration.py for a list of all supported configuration parameters.
configuration = datadog_api_client.v1.Configuration(
    host = "https://api.datadoghq.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')
```

Here's an example of authenticating with an endpoint:

```python

# Enter a context with an instance of the API client
with datadog_api_client.v1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aws_integration_api.AWSIntegrationApi(api_client)
    body = AWSAccount(
        access_key_id="access_key_id_example",
        account_id="1234567",
        account_specific_namespace_rules={
            "key": True,
        },
        excluded_regions=["us-east-1","us-west-2"],
        filter_tags=["<KEY>:<VALUE>"],
        host_tags=["<KEY>:<VALUE>"],
        role_name="DatadogAWSIntegrationRole",
        secret_access_key="secret_access_key_example",
    ) # AWSAccount | AWS Request Object

    # example passing only required values which don't have defaults set
    try:
        # Create an AWS integration
        api_response = api_instance.create_aws_account(body)
        pprint(api_response)
    except datadog_api_client.v1.ApiException as e:
        print("Exception when calling AWSIntegrationApi->create_aws_account: %s\n" % e)
```

## Getting Started

<!--- we need to add a working getting started example here, but which one? Do we know what the most used endpoint is? In datadogpy, we do sending an event, which would work too. Or we can add more than one. --->

### Documentation for API Endpoints and Models

Documentation for API endpoints and models can be found under the [`docs`](/docs) directory. 

### Unstable Endpoints

This client includes access to Datadog API endpoints while they are in an unstable state and may undergo breaking changes. An extra configuration step is required to enable these endpoints:

```python
configuration.unstable_operations["<OperationName>"] = True
```

where `<OperationName>` is the name of the method used to interact with that endpoint. For example: `list_log_indexes`, or `get_logs_index`

## Troubleshooting

For troubleshooting help, check out [our documentation](https://docs.datadoghq.com/api/), [file an issue](https://github.com/DataDog/datadog-api-client-python/issues) in this repo, or contact our [awesome support team](https://www.datadoghq.com/support/).

## Author

support@datadoghq.com

