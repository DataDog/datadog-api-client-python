"""
Create a RUM operation returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_operations_api import RUMOperationsApi
from datadog_api_client.v2.model.rum_operation_create_request import RUMOperationCreateRequest
from datadog_api_client.v2.model.rum_operation_create_request_data import RUMOperationCreateRequestData
from datadog_api_client.v2.model.rum_operation_journey_node import RUMOperationJourneyNode
from datadog_api_client.v2.model.rum_operation_journey_rum import RUMOperationJourneyRum
from datadog_api_client.v2.model.rum_operation_journey_step import RUMOperationJourneyStep
from datadog_api_client.v2.model.rum_operation_journey_step_type import RUMOperationJourneyStepType
from datadog_api_client.v2.model.rum_operation_request_attributes import RUMOperationRequestAttributes
from datadog_api_client.v2.model.rum_operation_type import RUMOperationType

body = RUMOperationCreateRequest(
    data=RUMOperationCreateRequestData(
        type=RUMOperationType.OPERATIONS,
        attributes=RUMOperationRequestAttributes(
            name="bdd_examplerumoperation",
            display_name="BDD operation",
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
    response = api_instance.create_rum_operation(body=body)

    print(response)
