"""
Update App Favorite Status returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.app_builder_api import AppBuilderApi
from datadog_api_client.v2.model.app_favorite_type import AppFavoriteType
from datadog_api_client.v2.model.update_app_favorite_request import UpdateAppFavoriteRequest
from datadog_api_client.v2.model.update_app_favorite_request_data import UpdateAppFavoriteRequestData
from datadog_api_client.v2.model.update_app_favorite_request_data_attributes import (
    UpdateAppFavoriteRequestDataAttributes,
)
from uuid import UUID

body = UpdateAppFavoriteRequest(
    data=UpdateAppFavoriteRequestData(
        attributes=UpdateAppFavoriteRequestDataAttributes(
            favorite=True,
        ),
        type=AppFavoriteType.FAVORITES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AppBuilderApi(api_client)
    api_instance.update_app_favorite(app_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body)
