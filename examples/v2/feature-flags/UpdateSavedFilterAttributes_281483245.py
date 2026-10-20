"""
Patch a saved filter updates only the description of a saved list
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi
from datadog_api_client.v2.model.patch_saved_filter_attributes import PatchSavedFilterAttributes
from datadog_api_client.v2.model.patch_saved_filter_data import PatchSavedFilterData
from datadog_api_client.v2.model.patch_saved_filter_request import PatchSavedFilterRequest
from datadog_api_client.v2.model.saved_filter_data_type import SavedFilterDataType
from uuid import UUID

body = PatchSavedFilterRequest(
    data=PatchSavedFilterData(
        type=SavedFilterDataType.SAVED_FILTERS,
        attributes=PatchSavedFilterAttributes(
            description="Updated synthetic test description.",
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    response = api_instance.update_saved_filter_attributes(
        saved_filter_id=UUID("d8e3a81b-1505-4600-99c6-c563d01d46b1"), body=body
    )

    print(response)
