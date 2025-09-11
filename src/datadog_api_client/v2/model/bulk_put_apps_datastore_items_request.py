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
    from datadog_api_client.v2.model.bulk_put_apps_datastore_items_request_data import (
        BulkPutAppsDatastoreItemsRequestData,
    )


class BulkPutAppsDatastoreItemsRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.bulk_put_apps_datastore_items_request_data import (
            BulkPutAppsDatastoreItemsRequestData,
        )

        return {
            "data": (BulkPutAppsDatastoreItemsRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[BulkPutAppsDatastoreItemsRequestData, UnsetType] = unset, **kwargs):
        """
        Request to insert multiple items into a datastore in a single operation.

        :param data: Data wrapper containing the items to insert and their configuration for the bulk insert operation.
        :type data: BulkPutAppsDatastoreItemsRequestData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
