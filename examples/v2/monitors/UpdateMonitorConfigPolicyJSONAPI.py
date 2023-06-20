"""
Edit a monitor configuration policy returns "OK" response using JSON:API models
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.monitors_api import MonitorsApi
from datadog_api_client.v2.model.monitor_config_policy_edit_request import MonitorConfigPolicyEditRequestJSON
from datadog_api_client.v2.model.monitor_config_policy_tag_policy import MonitorConfigPolicyTagPolicy
from datadog_api_client.v2.model.monitor_config_policy_type import MonitorConfigPolicyType

# there is a valid "monitor_configuration_policy" in the system
MONITOR_CONFIGURATION_POLICY_DATA_ID = environ["MONITOR_CONFIGURATION_POLICY_DATA_ID"]

body = MonitorConfigPolicyEditRequestJSON(
    id=MONITOR_CONFIGURATION_POLICY_DATA_ID,
    policy=MonitorConfigPolicyTagPolicy(
        tag_key="examplemonitor",
        tag_key_required=False,
        valid_tag_values=[
            "prod",
            "staging",
        ],
    ),
    policy_type=MonitorConfigPolicyType.TAG,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.update_monitor_config_policy(policy_id=MONITOR_CONFIGURATION_POLICY_DATA_ID, body=body)

    print(response)
