"""
Create allocation for a flag in an environment returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi
from datadog_api_client.v2.model.allocation_data_request import AllocationDataRequest
from datadog_api_client.v2.model.allocation_data_type import AllocationDataType
from datadog_api_client.v2.model.allocation_type import AllocationType
from datadog_api_client.v2.model.create_allocations_request import CreateAllocationsRequest
from datadog_api_client.v2.model.upsert_allocation_request import UpsertAllocationRequest
from datadog_api_client.v2.model.variant_weight_request import VariantWeightRequest

# there is a valid "feature_flag" in the system
FEATURE_FLAG_DATA_ATTRIBUTES_VARIANTS_0_ID = environ["FEATURE_FLAG_DATA_ATTRIBUTES_VARIANTS_0_ID"]
FEATURE_FLAG_DATA_ID = environ["FEATURE_FLAG_DATA_ID"]

# there is a valid "environment" in the system
ENVIRONMENT_DATA_ID = environ["ENVIRONMENT_DATA_ID"]

body = CreateAllocationsRequest(
    data=AllocationDataRequest(
        type=AllocationDataType.ALLOCATIONS,
        attributes=UpsertAllocationRequest(
            name="New targeting rule Example-Feature-Flag",
            key="new-targeting-rule-example-feature-flag",
            targeting_rules=[],
            variant_weights=[
                VariantWeightRequest(
                    variant_id=FEATURE_FLAG_DATA_ATTRIBUTES_VARIANTS_0_ID,
                    value=100.0,
                ),
            ],
            guardrail_metrics=[],
            type=AllocationType.CANARY,
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    response = api_instance.create_allocations_for_feature_flag_in_environment(
        feature_flag_id=FEATURE_FLAG_DATA_ID, environment_id=ENVIRONMENT_DATA_ID, body=body
    )

    print(response)
