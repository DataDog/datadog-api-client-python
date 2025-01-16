"""
Create a custom framework returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.create_custom_framework_request import CreateCustomFrameworkRequest
from datadog_api_client.v2.model.framework_control import FrameworkControl
from datadog_api_client.v2.model.framework_requirement import FrameworkRequirement

body = CreateCustomFrameworkRequest(
    handle="",
    name="",
    requirements=[
        FrameworkRequirement(
            controls=[
                FrameworkControl(
                    name="",
                    rule_ids=[
                        "",
                    ],
                ),
            ],
            name="",
        ),
    ],
    version="",
)

configuration = Configuration()
configuration.unstable_operations["create_custom_framework"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    api_instance.create_custom_framework(body=body)
