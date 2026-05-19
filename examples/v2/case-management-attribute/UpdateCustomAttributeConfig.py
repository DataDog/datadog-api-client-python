"""
Update custom attribute config returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_attribute_api import CaseManagementAttributeApi
from datadog_api_client.v2.model.custom_attribute_config_resource_type import CustomAttributeConfigResourceType
from datadog_api_client.v2.model.custom_attribute_config_update import CustomAttributeConfigUpdate
from datadog_api_client.v2.model.custom_attribute_config_update_attributes import CustomAttributeConfigUpdateAttributes
from datadog_api_client.v2.model.custom_attribute_config_update_request import CustomAttributeConfigUpdateRequest
from datadog_api_client.v2.model.custom_attribute_select_option import CustomAttributeSelectOption
from datadog_api_client.v2.model.custom_attribute_type import CustomAttributeType
from datadog_api_client.v2.model.custom_attribute_type_data import CustomAttributeTypeData

body = CustomAttributeConfigUpdateRequest(
    data=CustomAttributeConfigUpdate(
        attributes=CustomAttributeConfigUpdateAttributes(
            description="Updated description.",
            display_name="AWS Region",
            type=CustomAttributeType.NUMBER,
            type_data=CustomAttributeTypeData(
                options=[
                    CustomAttributeSelectOption(
                        value="us-east-1",
                    ),
                ],
            ),
        ),
        type=CustomAttributeConfigResourceType.CUSTOM_ATTRIBUTE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_custom_attribute_config"] = True
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementAttributeApi(api_client)
    response = api_instance.update_custom_attribute_config(
        case_type_id="case_type_id", custom_attribute_id="custom_attribute_id", body=body
    )

    print(response)
