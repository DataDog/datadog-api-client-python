"""
Create outcomes batch returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_scorecards_api import ServiceScorecardsApi
from datadog_api_client.v2.model.outcomes_batch_attributes import OutcomesBatchAttributes
from datadog_api_client.v2.model.outcomes_batch_request import OutcomesBatchRequest
from datadog_api_client.v2.model.outcomes_batch_request_data import OutcomesBatchRequestData
from datadog_api_client.v2.model.outcomes_batch_request_item import OutcomesBatchRequestItem
from datadog_api_client.v2.model.outcomes_batch_type import OutcomesBatchType
from datadog_api_client.v2.model.state import State

# there is a valid "create_scorecard_rule" in the system
CREATE_SCORECARD_RULE_DATA_ID = environ["CREATE_SCORECARD_RULE_DATA_ID"]

body = OutcomesBatchRequest(
    data=OutcomesBatchRequestData(
        attributes=OutcomesBatchAttributes(
            results=[
                OutcomesBatchRequestItem(
                    remarks='See: <a href="https://app.datadoghq.com/services">Services</a>',
                    rule_id=CREATE_SCORECARD_RULE_DATA_ID,
                    service_name="my-service",
                    state=State.PASS,
                ),
            ],
        ),
        type=OutcomesBatchType.BATCHED_OUTCOME,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_scorecard_outcomes_batch"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceScorecardsApi(api_client)
    response = api_instance.create_scorecard_outcomes_batch(body=body)

    print(response)
