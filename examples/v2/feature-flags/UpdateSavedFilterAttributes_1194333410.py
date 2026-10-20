"""
Patch a saved filter updates metadata and rules together
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi
from datadog_api_client.v2.model.patch_saved_filter_attributes import PatchSavedFilterAttributes
from datadog_api_client.v2.model.patch_saved_filter_data import PatchSavedFilterData
from datadog_api_client.v2.model.patch_saved_filter_request import PatchSavedFilterRequest
from datadog_api_client.v2.model.saved_filter_condition_operator import SavedFilterConditionOperator
from datadog_api_client.v2.model.saved_filter_condition_request import SavedFilterConditionRequest
from datadog_api_client.v2.model.saved_filter_data_type import SavedFilterDataType
from datadog_api_client.v2.model.saved_filter_targeting_rule_request import SavedFilterTargetingRuleRequest
from uuid import UUID

body = PatchSavedFilterRequest(
    data=PatchSavedFilterData(
        type=SavedFilterDataType.SAVED_FILTERS,
        attributes=PatchSavedFilterAttributes(
            name="patchSavedFilterTest-combined-157e7ff3",
            description="Combined synthetic test update.",
            targeting_rules=[
                SavedFilterTargetingRuleRequest(
                    conditions=[
                        SavedFilterConditionRequest(
                            operator=SavedFilterConditionOperator.ONE_OF,
                            attribute="org_id",
                            value=[
                                "test-org-1",
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    response = api_instance.update_saved_filter_attributes(
        saved_filter_id=UUID("2cfc7949-7eb4-4d76-b1b8-d1aa9b565535"), body=body
    )

    print(response)
