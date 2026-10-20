"""
Patch a saved filter accepts the current timestamp for metadata
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi
from datadog_api_client.v2.model.patch_saved_filter_attributes import PatchSavedFilterAttributes
from datadog_api_client.v2.model.patch_saved_filter_data import PatchSavedFilterData
from datadog_api_client.v2.model.patch_saved_filter_request import PatchSavedFilterRequest
from datadog_api_client.v2.model.saved_filter_data_type import SavedFilterDataType
from datetime import datetime
from dateutil.tz import tzutc
from uuid import UUID

body = PatchSavedFilterRequest(
    data=PatchSavedFilterData(
        attributes=PatchSavedFilterAttributes(
            description="Metadata with current timestamp.",
            last_updated_at=datetime(2026, 10, 16, 20, 20, 29, tzinfo=tzutc()),
        ),
        type=SavedFilterDataType.SAVED_FILTERS,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    response = api_instance.update_saved_filter_attributes(
        saved_filter_id=UUID("a8c393b4-3a9c-48fd-aa48-402c97e8d9c9"), body=body
    )

    print(response)
