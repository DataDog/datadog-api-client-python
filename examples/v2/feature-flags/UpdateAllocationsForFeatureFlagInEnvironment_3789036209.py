"""
Update targeting rules for a flag in an environment returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi
from datadog_api_client.v2.model.allocation_data_request import AllocationDataRequest
from datadog_api_client.v2.model.allocation_data_type import AllocationDataType
from datadog_api_client.v2.model.allocation_type import AllocationType
from datadog_api_client.v2.model.exposure_rollout_step_request import ExposureRolloutStepRequest
from datadog_api_client.v2.model.exposure_schedule_request import ExposureScheduleRequest
from datadog_api_client.v2.model.overwrite_allocations_request import OverwriteAllocationsRequest
from datadog_api_client.v2.model.rollout_options_request import RolloutOptionsRequest
from datadog_api_client.v2.model.rollout_strategy import RolloutStrategy
from datadog_api_client.v2.model.upsert_allocation_request import UpsertAllocationRequest
from datadog_api_client.v2.model.variant_weight_request import VariantWeightRequest

# there is a valid "feature_flag" in the system
FEATURE_FLAG_DATA_ATTRIBUTES_VARIANTS_0_ID = environ["FEATURE_FLAG_DATA_ATTRIBUTES_VARIANTS_0_ID"]
FEATURE_FLAG_DATA_ID = environ["FEATURE_FLAG_DATA_ID"]

# there is a valid "environment" in the system
ENVIRONMENT_DATA_ID = environ["ENVIRONMENT_DATA_ID"]

body = OverwriteAllocationsRequest(
    data=[
        AllocationDataRequest(
            type=AllocationDataType.ALLOCATIONS,
            attributes=UpsertAllocationRequest(
                key="overwrite-allocation-example-feature-flag",
                name="New targeting rule Example-Feature-Flag",
                targeting_rules=[],
                variant_weights=[
                    VariantWeightRequest(
                        variant_id=FEATURE_FLAG_DATA_ATTRIBUTES_VARIANTS_0_ID,
                        value=100.0,
                    ),
                ],
                exposure_schedule=ExposureScheduleRequest(
                    rollout_options=RolloutOptionsRequest(
                        strategy=RolloutStrategy.UNIFORM_INTERVALS,
                        autostart=False,
                        selection_interval_ms=86400000,
                    ),
                    rollout_steps=[
                        ExposureRolloutStepRequest(
                            exposure_ratio=0.05,
                            interval_ms=None,
                            is_pause_record=False,
                            grouped_step_index=0,
                        ),
                        ExposureRolloutStepRequest(
                            exposure_ratio=0.25,
                            interval_ms=None,
                            is_pause_record=False,
                            grouped_step_index=1,
                        ),
                        ExposureRolloutStepRequest(
                            exposure_ratio=1.0,
                            interval_ms=None,
                            is_pause_record=False,
                            grouped_step_index=2,
                        ),
                    ],
                ),
                guardrail_metrics=[],
                type=AllocationType.CANARY,
            ),
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    response = api_instance.update_allocations_for_feature_flag_in_environment(
        feature_flag_id=FEATURE_FLAG_DATA_ID, environment_id=ENVIRONMENT_DATA_ID, body=body
    )

    print(response)
