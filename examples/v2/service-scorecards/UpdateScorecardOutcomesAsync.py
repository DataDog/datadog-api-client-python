"""
Update Scorecard outcomes asynchronously returns "Accepted" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_scorecards_api import ServiceScorecardsApi
from datadog_api_client.v2.model.state import State
from datadog_api_client.v2.model.update_outcomes_async_attributes import UpdateOutcomesAsyncAttributes
from datadog_api_client.v2.model.update_outcomes_async_request import UpdateOutcomesAsyncRequest
from datadog_api_client.v2.model.update_outcomes_async_request_data import UpdateOutcomesAsyncRequestData
from datadog_api_client.v2.model.update_outcomes_async_request_item import UpdateOutcomesAsyncRequestItem
from datadog_api_client.v2.model.update_outcomes_async_type import UpdateOutcomesAsyncType

# there is a valid "create_scorecard_rule" in the system
CREATE_SCORECARD_RULE_DATA_ID = environ["CREATE_SCORECARD_RULE_DATA_ID"]

body = UpdateOutcomesAsyncRequest(
    data=UpdateOutcomesAsyncRequestData(
        attributes=UpdateOutcomesAsyncAttributes(
            results=[
                UpdateOutcomesAsyncRequestItem(
                    rule_id=CREATE_SCORECARD_RULE_DATA_ID,
                    entity_reference="service:my-service",
                    remarks='See: <a href="https://app.datadoghq.com/services">Services</a>',
                    state=State.PASS,
                ),
            ],
        ),
        type=UpdateOutcomesAsyncType.BATCHED_OUTCOME,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_scorecard_outcomes_async"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceScorecardsApi(api_client)
    api_instance.update_scorecard_outcomes_async(body=body)
