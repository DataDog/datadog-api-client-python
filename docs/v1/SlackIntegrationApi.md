# datadog_api_client.v1.SlackIntegrationApi

All URIs are relative to *https://api.datadoghq.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_slack_integration_channel**](SlackIntegrationApi.md#create_slack_integration_channel) | **POST** /api/v1/integration/slack/configuration/accounts/{account_name}/channels | Create a Slack integration channel
[**get_slack_integration_channel**](SlackIntegrationApi.md#get_slack_integration_channel) | **GET** /api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name} | Get a Slack integration channel
[**get_slack_integration_channels**](SlackIntegrationApi.md#get_slack_integration_channels) | **GET** /api/v1/integration/slack/configuration/accounts/{account_name}/channels | Get all channels in a Slack integration
[**remove_slack_integration_channel**](SlackIntegrationApi.md#remove_slack_integration_channel) | **DELETE** /api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name} | Remove a Slack integration channel
[**update_slack_integration_channel**](SlackIntegrationApi.md#update_slack_integration_channel) | **PATCH** /api/v1/integration/slack/configuration/accounts/{account_name}/channels/{channel_name} | Update a Slack integration channel


# **create_slack_integration_channel**
> SlackIntegrationChannel create_slack_integration_channel(account_name, body)

Create a Slack integration channel

Add a channel to your Datadog-Slack integration.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import slack_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slack_integration_api.SlackIntegrationApi(api_client)
    account_name = "account_name_example"  # str | Your Slack account name.
    body = SlackIntegrationChannel(
        display=SlackIntegrationChannelDisplay(
            message=True,
            notified=True,
            snapshot=True,
            tags=True,
        ),
        name="#general",
    )  # SlackIntegrationChannel | Payload describing Slack channel to be created

    # example passing only required values which don't have defaults set
    try:
        # Create a Slack integration channel
        api_response = api_instance.create_slack_integration_channel(account_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlackIntegrationApi->create_slack_integration_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| Your Slack account name. |
 **body** | [**SlackIntegrationChannel**](SlackIntegrationChannel.md)| Payload describing Slack channel to be created |

### Return type

[**SlackIntegrationChannel**](SlackIntegrationChannel.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Authentication error |  -  |
**404** | Item Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_slack_integration_channel**
> SlackIntegrationChannel get_slack_integration_channel(account_name, channel_name)

Get a Slack integration channel

Get a channel configured for your Datadog-Slack integration.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import slack_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slack_integration_api.SlackIntegrationApi(api_client)
    account_name = "account_name_example"  # str | Your Slack account name.
    channel_name = "channel_name_example"  # str | The name of the Slack channel being operated on.

    # example passing only required values which don't have defaults set
    try:
        # Get a Slack integration channel
        api_response = api_instance.get_slack_integration_channel(account_name, channel_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlackIntegrationApi->get_slack_integration_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| Your Slack account name. |
 **channel_name** | **str**| The name of the Slack channel being operated on. |

### Return type

[**SlackIntegrationChannel**](SlackIntegrationChannel.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Authentication error |  -  |
**404** | Item Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_slack_integration_channels**
> SlackIntegrationChannels get_slack_integration_channels(account_name)

Get all channels in a Slack integration

Get a list of all channels configured for your Datadog-Slack integration.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import slack_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slack_integration_api.SlackIntegrationApi(api_client)
    account_name = "account_name_example"  # str | Your Slack account name.

    # example passing only required values which don't have defaults set
    try:
        # Get all channels in a Slack integration
        api_response = api_instance.get_slack_integration_channels(account_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlackIntegrationApi->get_slack_integration_channels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| Your Slack account name. |

### Return type

[**SlackIntegrationChannels**](SlackIntegrationChannels.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Authentication error |  -  |
**404** | Item Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **remove_slack_integration_channel**
> remove_slack_integration_channel(account_name, channel_name)

Remove a Slack integration channel

Remove a channel from your Datadog-Slack integration.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import slack_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slack_integration_api.SlackIntegrationApi(api_client)
    account_name = "account_name_example"  # str | Your Slack account name.
    channel_name = "channel_name_example"  # str | The name of the Slack channel being operated on.

    # example passing only required values which don't have defaults set
    try:
        # Remove a Slack integration channel
        api_instance.remove_slack_integration_channel(account_name, channel_name)
    except ApiException as e:
        print("Exception when calling SlackIntegrationApi->remove_slack_integration_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| Your Slack account name. |
 **channel_name** | **str**| The name of the Slack channel being operated on. |

### Return type

void (empty response body)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The channel was removed successfully. |  -  |
**400** | Bad Request |  -  |
**403** | Authentication error |  -  |
**404** | Item Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_slack_integration_channel**
> SlackIntegrationChannel update_slack_integration_channel(account_name, channel_name, body)

Update a Slack integration channel

Update a channel used in your Datadog-Slack integration.

### Example

* Api Key Authentication (apiKeyAuth):
* Api Key Authentication (appKeyAuth):
```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import slack_integration_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Defining the site is optional and defaults to datadoghq.com
if "DD_SITE" in os.environ:
    configuration.server_variables["site"] = os.environ["DD_SITE"]

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.getenv('DD_CLIENT_API_KEY')

# Configure API key authorization: appKeyAuth
configuration.api_key['appKeyAuth'] = os.getenv('DD_CLIENT_APP_KEY')

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slack_integration_api.SlackIntegrationApi(api_client)
    account_name = "account_name_example"  # str | Your Slack account name.
    channel_name = "channel_name_example"  # str | The name of the Slack channel being operated on.
    body = SlackIntegrationChannel(
        display=SlackIntegrationChannelDisplay(
            message=True,
            notified=True,
            snapshot=True,
            tags=True,
        ),
        name="#general",
    )  # SlackIntegrationChannel | Payload describing fields and values to be updated.

    # example passing only required values which don't have defaults set
    try:
        # Update a Slack integration channel
        api_response = api_instance.update_slack_integration_channel(account_name, channel_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SlackIntegrationApi->update_slack_integration_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| Your Slack account name. |
 **channel_name** | **str**| The name of the Slack channel being operated on. |
 **body** | [**SlackIntegrationChannel**](SlackIntegrationChannel.md)| Payload describing fields and values to be updated. |

### Return type

[**SlackIntegrationChannel**](SlackIntegrationChannel.md)

### Authorization

[apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Authentication error |  -  |
**404** | Item Not Found |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

