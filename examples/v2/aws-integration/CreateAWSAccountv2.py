"""
AWS Integration - Create account returns "AWS Account object" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi
from datadog_api_client.v2.model.aws_account_create import AWSAccountCreate
from datadog_api_client.v2.model.aws_account_create_attributes import AWSAccountCreateAttributes
from datadog_api_client.v2.model.aws_account_create_request import AWSAccountCreateRequest
from datadog_api_client.v2.model.aws_account_type import AWSAccountType
from datadog_api_client.v2.model.aws_auth_config import AWSAuthConfig
from datadog_api_client.v2.model.aws_lambda_forwarder import AWSLambdaForwarder
from datadog_api_client.v2.model.aws_logs import AWSLogs
from datadog_api_client.v2.model.aws_metrics import AWSMetrics
from datadog_api_client.v2.model.aws_namespace_tag_filter import AWSNamespaceTagFilter
from datadog_api_client.v2.model.aws_namespaces_list import AWSNamespacesList
from datadog_api_client.v2.model.aws_regions_list import AWSRegionsList
from datadog_api_client.v2.model.aws_resources import AWSResources
from datadog_api_client.v2.model.aws_traces import AWSTraces
from datadog_api_client.v2.model.awsx_ray_services_list import AWSXRayServicesList

body = AWSAccountCreateRequest(
    data=AWSAccountCreate(
        attributes=AWSAccountCreateAttributes(
            account_tags=[],
            auth_config=AWSAuthConfig(),
            aws_account_id="123456789012",
            aws_regions=AWSRegionsList(
                include_only=[
                    "us-east-1",
                ],
            ),
            logs_config=AWSLogs(
                lambda_forwarder=AWSLambdaForwarder(
                    lambdas=[],
                    sources=[
                        "s3",
                    ],
                ),
            ),
            metrics_config=AWSMetrics(
                namespace_filters=AWSNamespacesList(
                    exclude_only=[
                        "AWS/EC2",
                    ],
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
            resources_config=AWSResources(),
            traces_config=AWSTraces(
                xray_services=AWSXRayServicesList(
                    include_only=[
                        "AWS/AppSync",
                    ],
                ),
            ),
        ),
        type=AWSAccountType.AWS_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_aws_accountv2"] = True
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.create_aws_accountv2(body=body)

    print(response)
