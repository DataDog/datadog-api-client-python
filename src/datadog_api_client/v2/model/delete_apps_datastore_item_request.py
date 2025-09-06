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
    from datadog_api_client.v2.model.delete_apps_datastore_item_request_data import DeleteAppsDatastoreItemRequestData


class DeleteAppsDatastoreItemRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.delete_apps_datastore_item_request_data import (
            DeleteAppsDatastoreItemRequestData,
        )

        return {
            "data": (DeleteAppsDatastoreItemRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[DeleteAppsDatastoreItemRequestData, UnsetType] = unset, **kwargs):
        """
        Request to delete a specific item from a datastore by its primary key.

        :param data: Data wrapper containing the information needed to identify and delete a specific datastore item.
        :type data: DeleteAppsDatastoreItemRequestData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
