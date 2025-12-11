"""
Create an AWS account returns "AWS Account object" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi
from datadog_api_client.v2.model.aws_account_create_request import AWSAccountCreateRequest
from datadog_api_client.v2.model.aws_account_create_request_attributes import AWSAccountCreateRequestAttributes
from datadog_api_client.v2.model.aws_account_create_request_data import AWSAccountCreateRequestData
from datadog_api_client.v2.model.aws_account_partition import AWSAccountPartition
from datadog_api_client.v2.model.aws_account_type import AWSAccountType
from datadog_api_client.v2.model.aws_auth_config_role import AWSAuthConfigRole
from datadog_api_client.v2.model.aws_lambda_forwarder_config import AWSLambdaForwarderConfig
from datadog_api_client.v2.model.aws_lambda_forwarder_config_log_source_config import (
    AWSLambdaForwarderConfigLogSourceConfig,
)
from datadog_api_client.v2.model.aws_log_source_tag_filter import AWSLogSourceTagFilter
from datadog_api_client.v2.model.aws_logs_config import AWSLogsConfig
from datadog_api_client.v2.model.aws_metrics_config import AWSMetricsConfig
from datadog_api_client.v2.model.aws_namespace_tag_filter import AWSNamespaceTagFilter
from datadog_api_client.v2.model.aws_resources_config import AWSResourcesConfig
from datadog_api_client.v2.model.aws_traces_config import AWSTracesConfig
from datadog_api_client.v2.model.awsccm_config import AWSCCMConfig
from datadog_api_client.v2.model.data_export_config import DataExportConfig

body = AWSAccountCreateRequest(
    data=AWSAccountCreateRequestData(
        attributes=AWSAccountCreateRequestAttributes(
            account_tags=[
                "key:value",
            ],
            auth_config=AWSAuthConfigRole(
                role_name="DatadogIntegrationRole",
            ),
            aws_account_id="123456789012",
            aws_partition=AWSAccountPartition.AWS,
            ccm_config=AWSCCMConfig(
                data_export_configs=[
                    DataExportConfig(
                        bucket_name="my-bucket",
                        bucket_region="us-east-1",
                        report_name="my-report",
                        report_prefix="reports",
                        report_type="CUR2.0",
                    ),
                ],
            ),
            logs_config=AWSLogsConfig(
                lambda_forwarder=AWSLambdaForwarderConfig(
                    lambdas=[
                        "arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder",
                    ],
                    log_source_config=AWSLambdaForwarderConfigLogSourceConfig(
                        tag_filters=[
                            AWSLogSourceTagFilter(
                                source="s3",
                                tags=[
                                    "test:test",
                                ],
                            ),
                        ],
                    ),
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
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.create_aws_account(body=body)

    print(response)
