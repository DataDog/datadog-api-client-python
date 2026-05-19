"""
Bulk subscribe to sample log generation returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.sample_log_generation_bulk_subscription_attributes import (
    SampleLogGenerationBulkSubscriptionAttributes,
)
from datadog_api_client.v2.model.sample_log_generation_bulk_subscription_data import (
    SampleLogGenerationBulkSubscriptionData,
)
from datadog_api_client.v2.model.sample_log_generation_bulk_subscription_request import (
    SampleLogGenerationBulkSubscriptionRequest,
)
from datadog_api_client.v2.model.sample_log_generation_bulk_subscription_request_type import (
    SampleLogGenerationBulkSubscriptionRequestType,
)
from datadog_api_client.v2.model.sample_log_generation_duration import SampleLogGenerationDuration

body = SampleLogGenerationBulkSubscriptionRequest(
    data=SampleLogGenerationBulkSubscriptionData(
        attributes=SampleLogGenerationBulkSubscriptionAttributes(
            content_pack_ids=[
                "aws-cloudtrail",
            ],
            duration=SampleLogGenerationDuration.THREE_DAYS,
        ),
        type=SampleLogGenerationBulkSubscriptionRequestType.BULK_SUBSCRIPTION_REQUESTS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["bulk_create_sample_log_generation_subscriptions"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.bulk_create_sample_log_generation_subscriptions(body=body)

    print(response)
