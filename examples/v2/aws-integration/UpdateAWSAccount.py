"""
AWS Integration - Patch account config returns "AWS Account object" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi
from datadog_api_client.v2.model.aws_account_partition import AWSAccountPartition
from datadog_api_client.v2.model.aws_account_patch_request import AWSAccountPatchRequest
from datadog_api_client.v2.model.aws_account_patch_request_attributes import AWSAccountPatchRequestAttributes
from datadog_api_client.v2.model.aws_account_patch_request_data import AWSAccountPatchRequestData
from datadog_api_client.v2.model.aws_auth_config_role import AWSAuthConfigRole
from datadog_api_client.v2.model.aws_lambda_forwarder_config import AWSLambdaForwarderConfig
from datadog_api_client.v2.model.aws_logs_config import AWSLogsConfig
from datadog_api_client.v2.model.aws_metrics_config import AWSMetricsConfig
from datadog_api_client.v2.model.aws_namespace_filters_include_only import AWSNamespaceFiltersIncludeOnly
from datadog_api_client.v2.model.aws_namespace_tag_filter import AWSNamespaceTagFilter
from datadog_api_client.v2.model.aws_regions_include_only import AWSRegionsIncludeOnly
from datadog_api_client.v2.model.aws_resources_config import AWSResourcesConfig
from datadog_api_client.v2.model.aws_traces_config import AWSTracesConfig
from datadog_api_client.v2.model.x_ray_services_include_only import XRayServicesIncludeOnly

# there is a valid "aws_account_v2" in the system
AWS_ACCOUNT_V2_DATA_ATTRIBUTES_AWS_ACCOUNT_ID = environ["AWS_ACCOUNT_V2_DATA_ATTRIBUTES_AWS_ACCOUNT_ID"]

body = AWSAccountPatchRequest(
    data=AWSAccountPatchRequestData(
        attributes=AWSAccountPatchRequestAttributes(
            account_tags=[],
            auth_config=AWSAuthConfigRole(
                role_name="test",
            ),
            aws_account_id=AWS_ACCOUNT_V2_DATA_ATTRIBUTES_AWS_ACCOUNT_ID,
            aws_partition=AWSAccountPartition.AWS,
            aws_regions=AWSRegionsIncludeOnly(
                include_only=[
                    "us-east-1",
                ],
            ),
            logs_config=AWSLogsConfig(
                lambda_forwarder=AWSLambdaForwarderConfig(
                    lambdas=[],
                    sources=[
                        "s3",
                    ],
                ),
            ),
            metrics_config=AWSMetricsConfig(
                namespace_filters=AWSNamespaceFiltersIncludeOnly(
                    include_only=[
                        "AWS/EC2",
                    ],
                ),
                tag_filters=[
                    AWSNamespaceTagFilter(
                        namespace="AWS/EC2",
                        tags=[],
                    ),
                ],
            ),
            resources_config=AWSResourcesConfig(),
            traces_config=AWSTracesConfig(
                xray_services=XRayServicesIncludeOnly(
                    include_only=[
                        "AWS/AppSync",
                    ],
                ),
            ),
        ),
        id=AWS_ACCOUNT_V2_DATA_ATTRIBUTES_AWS_ACCOUNT_ID,
        type="account",
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_aws_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.update_aws_account(aws_account_id=AWS_ACCOUNT_V2_DATA_ATTRIBUTES_AWS_ACCOUNT_ID, body=body)

    print(response)
