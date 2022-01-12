# datadog_api_client.v2.CloudWorkloadSecurityApi

All URIs are relative to *https://api.datadoghq.com*

| Method                                                                                                                 | HTTP request                                                                               | Description                                   |
| ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------- |
| [**create_cloud_workload_security_agent_rule**](CloudWorkloadSecurityApi.md#create_cloud_workload_security_agent_rule) | **POST** /api/v2/security_monitoring/cloud_workload_security/agent_rules                   | Create a Cloud Workload Security Agent rule   |
| [**delete_cloud_workload_security_agent_rule**](CloudWorkloadSecurityApi.md#delete_cloud_workload_security_agent_rule) | **DELETE** /api/v2/security_monitoring/cloud_workload_security/agent_rules/{agent_rule_id} | Delete a Cloud Workload Security Agent rule   |
| [**download_cloud_workload_policy_file**](CloudWorkloadSecurityApi.md#download_cloud_workload_policy_file)             | **GET** /api/v2/security/cloud_workload/policy/download                                    | Get the latest Cloud Workload Security policy |
| [**get_cloud_workload_security_agent_rule**](CloudWorkloadSecurityApi.md#get_cloud_workload_security_agent_rule)       | **GET** /api/v2/security_monitoring/cloud_workload_security/agent_rules/{agent_rule_id}    | Get a Cloud Workload Security Agent rule      |
| [**list_cloud_workload_security_agent_rules**](CloudWorkloadSecurityApi.md#list_cloud_workload_security_agent_rules)   | **GET** /api/v2/security_monitoring/cloud_workload_security/agent_rules                    | Get all Cloud Workload Security Agent rules   |
| [**update_cloud_workload_security_agent_rule**](CloudWorkloadSecurityApi.md#update_cloud_workload_security_agent_rule) | **PATCH** /api/v2/security_monitoring/cloud_workload_security/agent_rules/{agent_rule_id}  | Update a Cloud Workload Security Agent rule   |

# **create_cloud_workload_security_agent_rule**

> CloudWorkloadSecurityAgentRuleResponse create_cloud_workload_security_agent_rule(body)

Create a new Agent rule with the given parameters.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import cloud_workload_security_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_workload_security_api.CloudWorkloadSecurityApi(api_client)
    body = CloudWorkloadSecurityAgentRuleCreateRequest(
        data=CloudWorkloadSecurityAgentRuleCreateData(
            attributes=CloudWorkloadSecurityAgentRuleCreateAttributes(
                description="My Agent rule",
                enabled=True,
                expression="exec.file.name == \"sh\"",
                name="my_agent_rule",
            ),
            type=CloudWorkloadSecurityAgentRuleType("agent_rule"),
        ),
    )  # CloudWorkloadSecurityAgentRuleCreateRequest | The definition of the new Agent rule.

    # example passing only required values which don't have defaults set
    try:
        # Create a Cloud Workload Security Agent rule
        api_response = api_instance.create_cloud_workload_security_agent_rule(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudWorkloadSecurityApi->create_cloud_workload_security_agent_rule: %s\n" % e)
```

### Parameters

| Name     | Type                                                                                              | Description                           | Notes |
| -------- | ------------------------------------------------------------------------------------------------- | ------------------------------------- | ----- |
| **body** | [**CloudWorkloadSecurityAgentRuleCreateRequest**](CloudWorkloadSecurityAgentRuleCreateRequest.md) | The definition of the new Agent rule. |

### Return type

[**CloudWorkloadSecurityAgentRuleResponse**](CloudWorkloadSecurityAgentRuleResponse.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **200**     | OK                | -                |
| **400**     | Bad Request       | -                |
| **403**     | Not Authorized    | -                |
| **409**     | Conflict          | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **delete_cloud_workload_security_agent_rule**

> delete_cloud_workload_security_agent_rule(agent_rule_id)

Delete a specific Agent rule.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import cloud_workload_security_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_workload_security_api.CloudWorkloadSecurityApi(api_client)
    agent_rule_id = "3b5-v82-ns6"  # str | The ID of the Agent rule.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Cloud Workload Security Agent rule
        api_instance.delete_cloud_workload_security_agent_rule(agent_rule_id)
    except ApiException as e:
        print("Exception when calling CloudWorkloadSecurityApi->delete_cloud_workload_security_agent_rule: %s\n" % e)
```

### Parameters

| Name              | Type    | Description               | Notes |
| ----------------- | ------- | ------------------------- | ----- |
| **agent_rule_id** | **str** | The ID of the Agent rule. |

### Return type

void (empty response body)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **204**     | OK                | -                |
| **403**     | Not Authorized    | -                |
| **404**     | Not Found         | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **download_cloud_workload_policy_file**

> file_type download_cloud_workload_policy_file()

The download endpoint generates a Cloud Workload Security policy file from your currently active
Cloud Workload Security rules, and downloads them as a .policy file. This file can then be deployed to
your agents to update the policy running in your environment.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import cloud_workload_security_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_workload_security_api.CloudWorkloadSecurityApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the latest Cloud Workload Security policy
        api_response = api_instance.download_cloud_workload_policy_file()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudWorkloadSecurityApi->download_cloud_workload_policy_file: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

**file_type**

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/yaml, application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **200**     | OK                | -                |
| **403**     | Not Authorized    | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **get_cloud_workload_security_agent_rule**

> CloudWorkloadSecurityAgentRuleResponse get_cloud_workload_security_agent_rule(agent_rule_id)

Get the details of a specific Agent rule.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import cloud_workload_security_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_workload_security_api.CloudWorkloadSecurityApi(api_client)
    agent_rule_id = "3b5-v82-ns6"  # str | The ID of the Agent rule.

    # example passing only required values which don't have defaults set
    try:
        # Get a Cloud Workload Security Agent rule
        api_response = api_instance.get_cloud_workload_security_agent_rule(agent_rule_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudWorkloadSecurityApi->get_cloud_workload_security_agent_rule: %s\n" % e)
```

### Parameters

| Name              | Type    | Description               | Notes |
| ----------------- | ------- | ------------------------- | ----- |
| **agent_rule_id** | **str** | The ID of the Agent rule. |

### Return type

[**CloudWorkloadSecurityAgentRuleResponse**](CloudWorkloadSecurityAgentRuleResponse.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **200**     | OK                | -                |
| **403**     | Not Authorized    | -                |
| **404**     | Not Found         | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **list_cloud_workload_security_agent_rules**

> CloudWorkloadSecurityAgentRulesListResponse list_cloud_workload_security_agent_rules()

Get the list of Agent rules.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import cloud_workload_security_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_workload_security_api.CloudWorkloadSecurityApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all Cloud Workload Security Agent rules
        api_response = api_instance.list_cloud_workload_security_agent_rules()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudWorkloadSecurityApi->list_cloud_workload_security_agent_rules: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**CloudWorkloadSecurityAgentRulesListResponse**](CloudWorkloadSecurityAgentRulesListResponse.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **200**     | OK                | -                |
| **403**     | Not Authorized    | -                |
| **429**     | Too many requests | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)

# **update_cloud_workload_security_agent_rule**

> CloudWorkloadSecurityAgentRuleResponse update_cloud_workload_security_agent_rule(agent_rule_id, body)

Update a specific Agent rule.
Returns the Agent rule object when the request is successful.

### Example

- OAuth Authentication (AuthZ):
- Api Key Authentication (apiKeyAuth):
- Api Key Authentication (appKeyAuth):

```python
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import cloud_workload_security_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_workload_security_api.CloudWorkloadSecurityApi(api_client)
    agent_rule_id = "3b5-v82-ns6"  # str | The ID of the Agent rule.
    body = CloudWorkloadSecurityAgentRuleUpdateRequest(
        data=CloudWorkloadSecurityAgentRuleUpdateData(
            attributes=CloudWorkloadSecurityAgentRuleUpdateAttributes(
                description="My Agent rule",
                enabled=True,
                expression="exec.file.name == \"sh\"",
            ),
            type=CloudWorkloadSecurityAgentRuleType("agent_rule"),
        ),
    )  # CloudWorkloadSecurityAgentRuleUpdateRequest | New definition of the Agent rule.

    # example passing only required values which don't have defaults set
    try:
        # Update a Cloud Workload Security Agent rule
        api_response = api_instance.update_cloud_workload_security_agent_rule(agent_rule_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudWorkloadSecurityApi->update_cloud_workload_security_agent_rule: %s\n" % e)
```

### Parameters

| Name              | Type                                                                                              | Description                       | Notes |
| ----------------- | ------------------------------------------------------------------------------------------------- | --------------------------------- | ----- |
| **agent_rule_id** | **str**                                                                                           | The ID of the Agent rule.         |
| **body**          | [**CloudWorkloadSecurityAgentRuleUpdateRequest**](CloudWorkloadSecurityAgentRuleUpdateRequest.md) | New definition of the Agent rule. |

### Return type

[**CloudWorkloadSecurityAgentRuleResponse**](CloudWorkloadSecurityAgentRuleResponse.md)

### Authorization

[AuthZ](README.md#AuthZ), [apiKeyAuth](README.md#apiKeyAuth), [appKeyAuth](README.md#appKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description             | Response headers |
| ----------- | ----------------------- | ---------------- |
| **200**     | OK                      | -                |
| **400**     | Bad Request             | -                |
| **403**     | Not Authorized          | -                |
| **404**     | Not Found               | -                |
| **409**     | Concurrent Modification | -                |
| **429**     | Too many requests       | -                |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to README]](README.md)
