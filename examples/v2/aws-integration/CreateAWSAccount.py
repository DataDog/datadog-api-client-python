"""
AWS Integration - Create account config returns "AWS Account object" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi
from datadog_api_client.v2.model.aws_account_create_request import AWSAccountCreateRequest
from datadog_api_client.v2.model.aws_account_create_request_attributes import AWSAccountCreateRequestAttributes
from datadog_api_client.v2.model.aws_account_create_request_data import AWSAccountCreateRequestData
from datadog_api_client.v2.model.aws_account_partition import AWSAccountPartition
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

body = AWSAccountCreateRequest(
    data=AWSAccountCreateRequestData(
        attributes=AWSAccountCreateRequestAttributes(
            account_tags=[],
            auth_config=AWSAuthConfigRole(
                role_name="test",
            ),
            aws_account_id="123456789012",
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
        id="123456789012",
        type="account",
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_aws_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.create_aws_account(body=body)

    print(response)
