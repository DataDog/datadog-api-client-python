"""
Create a custom framework returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.create_custom_framework_request import CreateCustomFrameworkRequest
from datadog_api_client.v2.model.custom_framework_control import CustomFrameworkControl
from datadog_api_client.v2.model.custom_framework_data import CustomFrameworkData
from datadog_api_client.v2.model.custom_framework_data_attributes import CustomFrameworkDataAttributes
from datadog_api_client.v2.model.custom_framework_requirement import CustomFrameworkRequirement
from datadog_api_client.v2.model.custom_framework_type import CustomFrameworkType

body = CreateCustomFrameworkRequest(
    data=CustomFrameworkData(
        type=CustomFrameworkType.CUSTOM_FRAMEWORK,
        attributes=CustomFrameworkDataAttributes(
            name="name",
            handle="create-framework-new",
            version="10",
            icon_url="test-url",
            requirements=[
                CustomFrameworkRequirement(
                    name="requirement",
                    controls=[
                        CustomFrameworkControl(
                            name="control",
                            rules_id=[
                                "def-000-be9",
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_custom_framework(body=body)

    print(response)
