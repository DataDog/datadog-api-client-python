"""
Update an AWS integration returns "AWS Account object" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi
from datadog_api_client.v2.model.aws_account_partition import AWSAccountPartition
from datadog_api_client.v2.model.aws_account_type import AWSAccountType
from datadog_api_client.v2.model.aws_account_update_request import AWSAccountUpdateRequest
from datadog_api_client.v2.model.aws_account_update_request_attributes import AWSAccountUpdateRequestAttributes
from datadog_api_client.v2.model.aws_account_update_request_data import AWSAccountUpdateRequestData
from datadog_api_client.v2.model.aws_auth_config_role import AWSAuthConfigRole
from datadog_api_client.v2.model.aws_lambda_forwarder_config import AWSLambdaForwarderConfig
from datadog_api_client.v2.model.aws_logs_config import AWSLogsConfig
from datadog_api_client.v2.model.aws_metrics_config import AWSMetricsConfig
from datadog_api_client.v2.model.aws_namespace_tag_filter import AWSNamespaceTagFilter
from datadog_api_client.v2.model.aws_resources_config import AWSResourcesConfig
from datadog_api_client.v2.model.aws_traces_config import AWSTracesConfig

# there is a valid "aws_account_v2" in the system
AWS_ACCOUNT_V2_DATA_ID = environ["AWS_ACCOUNT_V2_DATA_ID"]

body = AWSAccountUpdateRequest(
    data=AWSAccountUpdateRequestData(
        attributes=AWSAccountUpdateRequestAttributes(
            account_tags=[
                "key:value",
            ],
            auth_config=AWSAuthConfigRole(
                role_name="DatadogIntegrationRole",
            ),
            aws_account_id="123456789012",
            aws_partition=AWSAccountPartition.AWS,
            logs_config=AWSLogsConfig(
                lambda_forwarder=AWSLambdaForwarderConfig(
                    lambdas=[
                        "arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder",
                    ],
                    sources=[
                        "s3",
                    ],
                ),
            ),
            metrics_config=AWSMetricsConfig(
                automute_enabled=True,
                collect_cloudwatch_alarms=True,
                collect_custom_metrics=True,
                enabled=True,
                tag_filters=[
                    AWSNamespaceTagFilter(
                        namespace="AWS/EC2",
                        tags=[
                            "key:value",
                        ],
                    ),
                ],
            ),
            resources_config=AWSResourcesConfig(
                cloud_security_posture_management_collection=False,
                extended_collection=False,
            ),
            traces_config=AWSTracesConfig(),
        ),
        type=AWSAccountType.ACCOUNT,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_aws_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.update_aws_account(aws_account_config_id=AWS_ACCOUNT_V2_DATA_ID, body=body)

    print(response)
