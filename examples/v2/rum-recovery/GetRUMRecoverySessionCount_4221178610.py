"""
Count recoverable sessions accepts exactly 180 days
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_recovery_api import RUMRecoveryApi
from datadog_api_client.v2.model.rum_recovery_count_attributes import RumRecoveryCountAttributes
from datadog_api_client.v2.model.rum_recovery_count_request import RumRecoveryCountRequest
from datadog_api_client.v2.model.rum_recovery_count_request_data import RumRecoveryCountRequestData

body = RumRecoveryCountRequest(
    data=RumRecoveryCountRequestData(
        type="rum_recovery_count",
        attributes=RumRecoveryCountAttributes(
            query="service:rum18600-fixture",
            _from=1621077071000,
            to=1636629071000,
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMRecoveryApi(api_client)
    response = api_instance.get_rum_recovery_session_count(body=body)

    print(response)
