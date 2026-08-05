"""
Patch a deployment event by version returns "Accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dora_metrics_api import DORAMetricsApi
from datadog_api_client.v2.model.dora_deployment_patch_by_version_request import DORADeploymentPatchByVersionRequest
from datadog_api_client.v2.model.dora_deployment_patch_by_version_request_attributes import (
    DORADeploymentPatchByVersionRequestAttributes,
)
from datadog_api_client.v2.model.dora_deployment_patch_by_version_request_data import (
    DORADeploymentPatchByVersionRequestData,
)
from datadog_api_client.v2.model.dora_deployment_patch_remediation import DORADeploymentPatchRemediation
from datadog_api_client.v2.model.dora_deployment_patch_remediation_type import DORADeploymentPatchRemediationType
from datadog_api_client.v2.model.dora_deployment_patch_request_data_type import DORADeploymentPatchRequestDataType

body = DORADeploymentPatchByVersionRequest(
    data=DORADeploymentPatchByVersionRequestData(
        attributes=DORADeploymentPatchByVersionRequestAttributes(
            change_failure=True,
            env="production",
            remediation=DORADeploymentPatchRemediation(
                type=DORADeploymentPatchRemediationType.ROLLBACK,
            ),
            service="my-service",
            version="v1.2.3",
        ),
        type=DORADeploymentPatchRequestDataType.DORA_DEPLOYMENT_PATCH_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["patch_dora_deployment_by_version"] = True
with ApiClient(configuration) as api_client:
    api_instance = DORAMetricsApi(api_client)
    api_instance.patch_dora_deployment_by_version(body=body)
