"""
Create an enrollment returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_prem_management_service_api import OnPremManagementServiceApi
from datadog_api_client.v2.model.on_prem_management_service_create_enrollment_request import (
    OnPremManagementServiceCreateEnrollmentRequest,
)
from datadog_api_client.v2.model.on_prem_management_service_enrollment_attributes import (
    OnPremManagementServiceEnrollmentAttributes,
)
from datadog_api_client.v2.model.on_prem_management_service_enrollment_attributes_runner_modes_items import (
    OnPremManagementServiceEnrollmentAttributesRunnerModesItems,
)
from datadog_api_client.v2.model.on_prem_management_service_enrollment_data_request import (
    OnPremManagementServiceEnrollmentDataRequest,
)
from datadog_api_client.v2.model.on_prem_management_service_enrollment_type import OnPremManagementServiceEnrollmentType

body = OnPremManagementServiceCreateEnrollmentRequest(
    data=OnPremManagementServiceEnrollmentDataRequest(
        attributes=OnPremManagementServiceEnrollmentAttributes(
            actions_allowlist=[
                "com.datadoghq.jenkins.*",
            ],
            runner_host="runner.example.com",
            runner_modes=[
                OnPremManagementServiceEnrollmentAttributesRunnerModesItems.WORKFLOW_AUTOMATION,
            ],
            runner_name="my-runner",
        ),
        type=OnPremManagementServiceEnrollmentType.ENROLLMENT,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_on_prem_management_service_enrollment"] = True
with ApiClient(configuration) as api_client:
    api_instance = OnPremManagementServiceApi(api_client)
    response = api_instance.create_on_prem_management_service_enrollment(body=body)

    print(response)
