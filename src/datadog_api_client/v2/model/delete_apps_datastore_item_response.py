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
    from datadog_api_client.v2.model.delete_apps_datastore_item_response_data import DeleteAppsDatastoreItemResponseData


class DeleteAppsDatastoreItemResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.delete_apps_datastore_item_response_data import (
            DeleteAppsDatastoreItemResponseData,
        )

        return {
            "data": (DeleteAppsDatastoreItemResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[DeleteAppsDatastoreItemResponseData, UnsetType] = unset, **kwargs):
        """
        Response from successfully deleting a datastore item.

        :param data: Data containing the identifier of the datastore item that was successfully deleted.
        :type data: DeleteAppsDatastoreItemResponseData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
