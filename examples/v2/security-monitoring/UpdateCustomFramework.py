"""
Update a custom framework returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.custom_framework_control import CustomFrameworkControl
from datadog_api_client.v2.model.custom_framework_data import CustomFrameworkData
from datadog_api_client.v2.model.custom_framework_data_attributes import CustomFrameworkDataAttributes
from datadog_api_client.v2.model.custom_framework_requirement import CustomFrameworkRequirement
from datadog_api_client.v2.model.custom_framework_type import CustomFrameworkType
from datadog_api_client.v2.model.update_custom_framework_request import UpdateCustomFrameworkRequest

body = UpdateCustomFrameworkRequest(
    data=CustomFrameworkData(
        attributes=CustomFrameworkDataAttributes(
            handle="",
            name="",
            requirements=[
                CustomFrameworkRequirement(
                    controls=[
                        CustomFrameworkControl(
                            name="",
                            rules_id=[
                                "",
                            ],
                        ),
                    ],
                    name="",
                ),
            ],
            version="",
        ),
        type=CustomFrameworkType.CUSTOM_FRAMEWORK,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_custom_framework"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.update_custom_framework(handle="handle", version="version", body=body)

    print(response)
