"""
Update a RUM operation returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_operations_api import RUMOperationsApi
from datadog_api_client.v2.model.rum_operation_journey_node import RUMOperationJourneyNode
from datadog_api_client.v2.model.rum_operation_journey_rum import RUMOperationJourneyRum
from datadog_api_client.v2.model.rum_operation_journey_step import RUMOperationJourneyStep
from datadog_api_client.v2.model.rum_operation_journey_step_type import RUMOperationJourneyStepType
from datadog_api_client.v2.model.rum_operation_request_attributes import RUMOperationRequestAttributes
from datadog_api_client.v2.model.rum_operation_type import RUMOperationType
from datadog_api_client.v2.model.rum_operation_update_request import RUMOperationUpdateRequest
from datadog_api_client.v2.model.rum_operation_update_request_data import RUMOperationUpdateRequestData

# there is a valid "rum_operation" in the system
RUM_OPERATION_DATA_ATTRIBUTES_NAME = environ["RUM_OPERATION_DATA_ATTRIBUTES_NAME"]
RUM_OPERATION_DATA_ID = environ["RUM_OPERATION_DATA_ID"]

body = RUMOperationUpdateRequest(
    data=RUMOperationUpdateRequestData(
        id=RUM_OPERATION_DATA_ID,
        type=RUMOperationType.OPERATIONS,
        attributes=RUMOperationRequestAttributes(
            name=RUM_OPERATION_DATA_ATTRIBUTES_NAME,
            display_name="BDD operation updated",
            tags=[
                "team:rum-backend",
            ],
            journey_rum=RUMOperationJourneyRum(
                rum_steps=[
                    RUMOperationJourneyStep(
                        type=RUMOperationJourneyStepType.START,
                        nodes=[
                            RUMOperationJourneyNode(
                                query="@type:action @action.type:click",
                            ),
                        ],
                    ),
                    RUMOperationJourneyStep(
                        type=RUMOperationJourneyStepType.STOP,
                        nodes=[
                            RUMOperationJourneyNode(
                                query="@type:view",
                            ),
                        ],
                    ),
                ],
            ),
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = RUMOperationsApi(api_client)
    response = api_instance.update_rum_operation(rum_operation_id=RUM_OPERATION_DATA_ID, body=body)

    print(response)
