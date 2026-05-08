"""
Update a dataset restriction returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dataset_restrictions_api import DatasetRestrictionsApi
from datadog_api_client.v2.model.dataset_restriction_ownership_mode import DatasetRestrictionOwnershipMode
from datadog_api_client.v2.model.dataset_restriction_restriction_mode import DatasetRestrictionRestrictionMode
from datadog_api_client.v2.model.dataset_restriction_update_request import DatasetRestrictionUpdateRequest
from datadog_api_client.v2.model.dataset_restriction_update_request_attributes import (
    DatasetRestrictionUpdateRequestAttributes,
)
from datadog_api_client.v2.model.dataset_restriction_update_request_data import DatasetRestrictionUpdateRequestData
from datadog_api_client.v2.model.dataset_restrictions_type import DatasetRestrictionsType

body = DatasetRestrictionUpdateRequest(
    data=DatasetRestrictionUpdateRequestData(
        attributes=DatasetRestrictionUpdateRequestAttributes(
            ownership_mode=DatasetRestrictionOwnershipMode.TEAM_TAG_BASED,
            restriction_mode=DatasetRestrictionRestrictionMode.DEFAULT_HIDE,
            unrestricted_principals=[],
        ),
        type=DatasetRestrictionsType.DATASET_RESTRICTIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_dataset_restriction"] = True
with ApiClient(configuration) as api_client:
    api_instance = DatasetRestrictionsApi(api_client)
    response = api_instance.update_dataset_restriction(product_type="product_type", body=body)

    print(response)
