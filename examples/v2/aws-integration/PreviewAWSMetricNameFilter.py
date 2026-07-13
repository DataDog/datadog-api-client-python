"""
Preview AWS metric name filter returns "AWS metric name filter preview result" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi
from datadog_api_client.v2.model.aws_metric_name_filter_preview_request import AWSMetricNameFilterPreviewRequest
from datadog_api_client.v2.model.aws_metric_name_filter_preview_request_attributes import (
    AWSMetricNameFilterPreviewRequestAttributes,
)
from datadog_api_client.v2.model.aws_metric_name_filter_preview_request_data import (
    AWSMetricNameFilterPreviewRequestData,
)
from datadog_api_client.v2.model.aws_metric_name_filter_preview_type import AWSMetricNameFilterPreviewType
from datadog_api_client.v2.model.aws_metric_name_filters_include_only import AWSMetricNameFiltersIncludeOnly

body = AWSMetricNameFilterPreviewRequest(
    data=AWSMetricNameFilterPreviewRequestData(
        attributes=AWSMetricNameFilterPreviewRequestAttributes(
            metric_name_filters=[
                AWSMetricNameFiltersIncludeOnly(
                    include_only=[
                        "aws.ec2.network_in",
                    ],
                    namespace="AWS/EC2",
                ),
            ],
        ),
        type=AWSMetricNameFilterPreviewType.METRIC_NAME_FILTER_PREVIEW,
    ),
)

configuration = Configuration()
configuration.unstable_operations["preview_aws_metric_name_filter"] = True
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.preview_aws_metric_name_filter(aws_account_config_id="aws_account_config_id", body=body)

    print(response)
