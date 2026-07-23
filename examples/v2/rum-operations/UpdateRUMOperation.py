"""
Update a RUM operation returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_operations_api import RUMOperationsApi
from datadog_api_client.v2.model.rum_operation_journey_composite_rule import RUMOperationJourneyCompositeRule
from datadog_api_client.v2.model.rum_operation_journey_composite_rule_kind import RUMOperationJourneyCompositeRuleKind
from datadog_api_client.v2.model.rum_operation_journey_node import RUMOperationJourneyNode
from datadog_api_client.v2.model.rum_operation_journey_predicate import RUMOperationJourneyPredicate
from datadog_api_client.v2.model.rum_operation_journey_rum import RUMOperationJourneyRum
from datadog_api_client.v2.model.rum_operation_journey_step import RUMOperationJourneyStep
from datadog_api_client.v2.model.rum_operation_journey_step_type import RUMOperationJourneyStepType
from datadog_api_client.v2.model.rum_operation_request_attributes import RUMOperationRequestAttributes
from datadog_api_client.v2.model.rum_operation_type import RUMOperationType
from datadog_api_client.v2.model.rum_operation_update_request import RUMOperationUpdateRequest
from datadog_api_client.v2.model.rum_operation_update_request_data import RUMOperationUpdateRequestData

body = RUMOperationUpdateRequest(
    data=RUMOperationUpdateRequestData(
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
        id="abc12345-1234-5678-abcd-ef1234567890",
        type=RUMOperationType.OPERATIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_rum_operation"] = True
with ApiClient(configuration) as api_client:
    api_instance = RUMOperationsApi(api_client)
    response = api_instance.update_rum_operation(operation_id="operation_id", body=body)

    print(response)
