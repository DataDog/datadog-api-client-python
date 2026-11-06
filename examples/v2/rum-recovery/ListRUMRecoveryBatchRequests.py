"""
List batch recovery requests returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_recovery_api import RUMRecoveryApi
from datadog_api_client.v2.model.rum_recovery_batch_request_type import RumRecoveryBatchRequestType

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMRecoveryApi(api_client)
    response = api_instance.list_rum_recovery_batch_requests(
        type=RumRecoveryBatchRequestType.BATCH,
    )

    print(response)
