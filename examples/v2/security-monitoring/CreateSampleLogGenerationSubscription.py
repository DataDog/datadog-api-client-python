"""
Subscribe to sample log generation returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.sample_log_generation_duration import SampleLogGenerationDuration
from datadog_api_client.v2.model.sample_log_generation_subscription_create_attributes import (
    SampleLogGenerationSubscriptionCreateAttributes,
)
from datadog_api_client.v2.model.sample_log_generation_subscription_create_data import (
    SampleLogGenerationSubscriptionCreateData,
)
from datadog_api_client.v2.model.sample_log_generation_subscription_create_request import (
    SampleLogGenerationSubscriptionCreateRequest,
)
from datadog_api_client.v2.model.sample_log_generation_subscription_request_type import (
    SampleLogGenerationSubscriptionRequestType,
)

body = SampleLogGenerationSubscriptionCreateRequest(
    data=SampleLogGenerationSubscriptionCreateData(
        attributes=SampleLogGenerationSubscriptionCreateAttributes(
            content_pack_id="aws-cloudtrail",
            duration=SampleLogGenerationDuration.THREE_DAYS,
        ),
        type=SampleLogGenerationSubscriptionRequestType.SUBSCRIPTION_REQUESTS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_sample_log_generation_subscription"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_sample_log_generation_subscription(body=body)

    print(response)
