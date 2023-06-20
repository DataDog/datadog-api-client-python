"""
Create a monitor configuration policy returns "OK" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi
from datadog_api_client.v2.model.monitor_config_policy_create_request import MonitorConfigPolicyCreateRequestJSON
from datadog_api_client.v2.model.monitor_config_policy_tag_policy_create_request import (
    MonitorConfigPolicyTagPolicyCreateRequest,
)
from datadog_api_client.v2.model.monitor_config_policy_type import MonitorConfigPolicyType

body = MonitorConfigPolicyCreateRequestJSON(
    policy_type=MonitorConfigPolicyType.TAG,
    policy=MonitorConfigPolicyTagPolicyCreateRequest(
        tag_key="examplemonitor",
        tag_key_required=False,
        valid_tag_values=[
            "prod",
            "staging",
        ],
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.create_monitor_config_policy(body=body)

    print(response)
