"""
Set the approval requirement for a feature flag returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi
from datadog_api_client.v2.model.feature_flag_approvals_data_type import FeatureFlagApprovalsDataType
from datadog_api_client.v2.model.update_feature_flag_approvals_attributes import UpdateFeatureFlagApprovalsAttributes
from datadog_api_client.v2.model.update_feature_flag_approvals_data import UpdateFeatureFlagApprovalsData
from datadog_api_client.v2.model.update_feature_flag_approvals_request import UpdateFeatureFlagApprovalsRequest
from uuid import UUID

body = UpdateFeatureFlagApprovalsRequest(
    data=UpdateFeatureFlagApprovalsData(
        attributes=UpdateFeatureFlagApprovalsAttributes(
            enabled=True,
        ),
        type=FeatureFlagApprovalsDataType.FEATURE_FLAG_APPROVALS,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    response = api_instance.update_feature_flag_approvals(
        feature_flag_id=UUID("550e8400-e29b-41d4-a716-446655440000"), body=body
    )

    print(response)
