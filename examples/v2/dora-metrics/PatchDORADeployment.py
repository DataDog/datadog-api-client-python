"""
Patch a deployment event returns "Accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dora_metrics_api import DORAMetricsApi
from datadog_api_client.v2.model.dora_deployment_patch_remediation import DORADeploymentPatchRemediation
from datadog_api_client.v2.model.dora_deployment_patch_remediation_type import DORADeploymentPatchRemediationType
from datadog_api_client.v2.model.dora_deployment_patch_request import DORADeploymentPatchRequest
from datadog_api_client.v2.model.dora_deployment_patch_request_attributes import DORADeploymentPatchRequestAttributes
from datadog_api_client.v2.model.dora_deployment_patch_request_data import DORADeploymentPatchRequestData
from datadog_api_client.v2.model.dora_deployment_patch_request_data_type import DORADeploymentPatchRequestDataType

body = DORADeploymentPatchRequest(
    data=DORADeploymentPatchRequestData(
        attributes=DORADeploymentPatchRequestAttributes(
            change_failure=True,
            remediation=DORADeploymentPatchRemediation(
                id="eG42zNIkVjM",
                type=DORADeploymentPatchRemediationType.ROLLBACK,
            ),
        ),
        id="z_RwVLi7v4Y",
        type=DORADeploymentPatchRequestDataType.DORA_DEPLOYMENT_PATCH_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DORAMetricsApi(api_client)
    api_instance.patch_dora_deployment(deployment_id="deployment_id", body=body)
