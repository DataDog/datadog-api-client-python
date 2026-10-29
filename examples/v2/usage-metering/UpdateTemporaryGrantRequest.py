"""
Decide a temporary grant request returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi
from datadog_api_client.v2.model.temporary_grant_request_decision import TemporaryGrantRequestDecision
from datadog_api_client.v2.model.temporary_grant_request_decision_attributes import (
    TemporaryGrantRequestDecisionAttributes,
)
from datadog_api_client.v2.model.temporary_grant_request_decision_data import TemporaryGrantRequestDecisionData
from datadog_api_client.v2.model.temporary_grant_request_decision_request import TemporaryGrantRequestDecisionRequest
from datadog_api_client.v2.model.temporary_grant_request_type import TemporaryGrantRequestType

# there is a valid "temporary_grant_request" in the system
TEMPORARY_GRANT_REQUEST_DATA_ID = environ["TEMPORARY_GRANT_REQUEST_DATA_ID"]

body = TemporaryGrantRequestDecisionRequest(
    data=TemporaryGrantRequestDecisionData(
        attributes=TemporaryGrantRequestDecisionAttributes(
            decision=TemporaryGrantRequestDecision.DENIED,
        ),
        id=TEMPORARY_GRANT_REQUEST_DATA_ID,
        type=TemporaryGrantRequestType.TEMPORARY_GRANT_REQUESTS,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_temporary_grant_request"] = True
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.update_temporary_grant_request(request_id=TEMPORARY_GRANT_REQUEST_DATA_ID, body=body)

    print(response)
