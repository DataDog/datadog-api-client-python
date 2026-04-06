"""
Create targeting rules for a flag env returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi
from datadog_api_client.v2.model.allocation_data_request import AllocationDataRequest
from datadog_api_client.v2.model.allocation_data_type import AllocationDataType
from datadog_api_client.v2.model.allocation_type import AllocationType
from datadog_api_client.v2.model.condition_operator import ConditionOperator
from datadog_api_client.v2.model.condition_request import ConditionRequest
from datadog_api_client.v2.model.create_allocations_request import CreateAllocationsRequest
from datadog_api_client.v2.model.exposure_rollout_step_request import ExposureRolloutStepRequest
from datadog_api_client.v2.model.exposure_schedule_request import ExposureScheduleRequest
from datadog_api_client.v2.model.guardrail_metric_request import GuardrailMetricRequest
from datadog_api_client.v2.model.guardrail_trigger_action import GuardrailTriggerAction
from datadog_api_client.v2.model.rollout_options_request import RolloutOptionsRequest
from datadog_api_client.v2.model.rollout_strategy import RolloutStrategy
from datadog_api_client.v2.model.targeting_rule_request import TargetingRuleRequest
from datadog_api_client.v2.model.upsert_allocation_request import UpsertAllocationRequest
from datadog_api_client.v2.model.variant_weight_request import VariantWeightRequest
from datetime import datetime
from dateutil.tz import tzutc
from uuid import UUID

body = CreateAllocationsRequest(
    data=AllocationDataRequest(
        attributes=UpsertAllocationRequest(
            experiment_id="550e8400-e29b-41d4-a716-446655440030",
            exposure_schedule=ExposureScheduleRequest(
                absolute_start_time=datetime(2025, 6, 13, 12, 0, tzinfo=tzutc()),
                control_variant_id="550e8400-e29b-41d4-a716-446655440012",
                control_variant_key="control",
                id=UUID("550e8400-e29b-41d4-a716-446655440010"),
                rollout_options=RolloutOptionsRequest(
                    autostart=False,
                    selection_interval_ms=3600000,
                    strategy=RolloutStrategy.UNIFORM_INTERVALS,
                ),
                rollout_steps=[
                    ExposureRolloutStepRequest(
                        exposure_ratio=0.5,
                        grouped_step_index=1,
                        id=UUID("550e8400-e29b-41d4-a716-446655440040"),
                        interval_ms=3600000,
                        is_pause_record=False,
                    ),
                ],
            ),
            guardrail_metrics=[
                GuardrailMetricRequest(
                    metric_id="metric-error-rate",
                    trigger_action=GuardrailTriggerAction.PAUSE,
                ),
            ],
            id=UUID("550e8400-e29b-41d4-a716-446655440020"),
            key="prod-rollout",
            name="Production Rollout",
            targeting_rules=[
                TargetingRuleRequest(
                    conditions=[
                        ConditionRequest(
                            attribute="user_tier",
                            operator=ConditionOperator.ONE_OF,
                            value=[
                                "premium",
                                "enterprise",
                            ],
                        ),
                    ],
                ),
            ],
            type=AllocationType.FEATURE_GATE,
            variant_weights=[
                VariantWeightRequest(
                    value=50.0,
                    variant_id=UUID("550e8400-e29b-41d4-a716-446655440001"),
                    variant_key="control",
                ),
            ],
        ),
        type=AllocationDataType.ALLOCATIONS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    response = api_instance.create_allocations_for_feature_flag_in_environment(
        feature_flag_id=UUID("550e8400-e29b-41d4-a716-446655440000"),
        environment_id=UUID("550e8400-e29b-41d4-a716-446655440001"),
        body=body,
    )

    print(response)
