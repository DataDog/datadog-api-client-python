"""
Create a RUM operation returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_operations_api import RUMOperationsApi
from datadog_api_client.v2.model.rum_operation_create_request import RUMOperationCreateRequest
from datadog_api_client.v2.model.rum_operation_create_request_data import RUMOperationCreateRequestData
from datadog_api_client.v2.model.rum_operation_journey_composite_rule import RUMOperationJourneyCompositeRule
from datadog_api_client.v2.model.rum_operation_journey_composite_rule_kind import RUMOperationJourneyCompositeRuleKind
from datadog_api_client.v2.model.rum_operation_journey_node import RUMOperationJourneyNode
from datadog_api_client.v2.model.rum_operation_journey_predicate import RUMOperationJourneyPredicate
from datadog_api_client.v2.model.rum_operation_journey_rum import RUMOperationJourneyRum
from datadog_api_client.v2.model.rum_operation_journey_step import RUMOperationJourneyStep
from datadog_api_client.v2.model.rum_operation_journey_step_type import RUMOperationJourneyStepType
from datadog_api_client.v2.model.rum_operation_request_attributes import RUMOperationRequestAttributes
from datadog_api_client.v2.model.rum_operation_type import RUMOperationType

body = RUMOperationCreateRequest(
    data=RUMOperationCreateRequestData(
        attributes=RUMOperationRequestAttributes(
            application_id=None,
            category=None,
            description=None,
            display_name="Checkout completed",
            feature_ids=[],
            journey_rum=RUMOperationJourneyRum(
                rum_steps=[
                    RUMOperationJourneyStep(
                        composite=RUMOperationJourneyCompositeRule(
                            kind=RUMOperationJourneyCompositeRuleKind.ALL_OF,
                            max_window_ms=30000,
                            predicates=[
                                RUMOperationJourneyPredicate(
                                    query="@type:action @action.type:click",
                                ),
                            ],
                        ),
                        nodes=[
                            RUMOperationJourneyNode(
                                query="@type:action @action.type:click",
                            ),
                        ],
                        type=RUMOperationJourneyStepType.START,
                    ),
                ],
            ),
            name="checkout_completed",
            tags=[
                "team:checkout",
            ],
        ),
        type=RUMOperationType.OPERATIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_rum_operation"] = True
with ApiClient(configuration) as api_client:
    api_instance = RUMOperationsApi(api_client)
    response = api_instance.create_rum_operation(body=body)

    print(response)
