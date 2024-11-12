"""
Create an AWS integration returns "AWS Account object" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi
from datadog_api_client.v2.model.aws_account_create_request import AWSAccountCreateRequest
from datadog_api_client.v2.model.aws_account_create_request_attributes import AWSAccountCreateRequestAttributes
from datadog_api_client.v2.model.aws_account_create_request_data import AWSAccountCreateRequestData
from datadog_api_client.v2.model.aws_account_partition import AWSAccountPartition
from datadog_api_client.v2.model.aws_account_type import AWSAccountType
from datadog_api_client.v2.model.aws_auth_config_keys import AWSAuthConfigKeys
from datadog_api_client.v2.model.aws_lambda_forwarder_config import AWSLambdaForwarderConfig
from datadog_api_client.v2.model.aws_logs_config import AWSLogsConfig
from datadog_api_client.v2.model.aws_metrics_config import AWSMetricsConfig
from datadog_api_client.v2.model.aws_namespace_tag_filter import AWSNamespaceTagFilter
from datadog_api_client.v2.model.aws_resources_config import AWSResourcesConfig
from datadog_api_client.v2.model.aws_traces_config import AWSTracesConfig

body = AWSAccountCreateRequest(
    data=AWSAccountCreateRequestData(
        attributes=AWSAccountCreateRequestAttributes(
            account_tags=[
                "key:value",
            ],
            auth_config=AWSAuthConfigKeys(
                access_key_id="AKIAIOSFODNN7EXAMPLE",
                secret_access_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
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
configuration.unstable_operations["create_aws_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.create_aws_account(body=body)

    print(response)
