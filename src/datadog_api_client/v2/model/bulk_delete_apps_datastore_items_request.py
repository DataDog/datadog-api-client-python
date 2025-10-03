# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.bulk_delete_apps_datastore_items_request_data import (
        BulkDeleteAppsDatastoreItemsRequestData,
    )


class BulkDeleteAppsDatastoreItemsRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.bulk_delete_apps_datastore_items_request_data import (
            BulkDeleteAppsDatastoreItemsRequestData,
        )

        return {
            "data": (BulkDeleteAppsDatastoreItemsRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[BulkDeleteAppsDatastoreItemsRequestData, UnsetType] = unset, **kwargs):
        """
        Request to delete items from a datastore.

        :param data: Data wrapper containing the data needed to delete items from a datastore.
        :type data: BulkDeleteAppsDatastoreItemsRequestData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
