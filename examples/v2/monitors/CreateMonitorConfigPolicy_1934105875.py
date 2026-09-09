"""
Create a downtime duration monitor configuration policy returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi
from datadog_api_client.v2.model.monitor_config_policy_attribute_create_request import (
    MonitorConfigPolicyAttributeCreateRequest,
)
from datadog_api_client.v2.model.monitor_config_policy_create_data import MonitorConfigPolicyCreateData
from datadog_api_client.v2.model.monitor_config_policy_create_request import MonitorConfigPolicyCreateRequest
from datadog_api_client.v2.model.monitor_config_policy_downtime_policy_create_request import (
    MonitorConfigPolicyDowntimePolicyCreateRequest,
)
from datadog_api_client.v2.model.monitor_config_policy_resource_type import MonitorConfigPolicyResourceType
from datadog_api_client.v2.model.monitor_config_policy_type import MonitorConfigPolicyType

body = MonitorConfigPolicyCreateRequest(
    data=MonitorConfigPolicyCreateData(
        attributes=MonitorConfigPolicyAttributeCreateRequest(
            policy_type=MonitorConfigPolicyType.DOWNTIME,
            policy=MonitorConfigPolicyDowntimePolicyCreateRequest(
                max_duration_ms=3600000,
            ),
        ),
        type=MonitorConfigPolicyResourceType.MONITOR_CONFIG_POLICY,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.create_monitor_config_policy(body=body)

    print(response)
