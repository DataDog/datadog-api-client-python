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
    from datadog_api_client.v2.model.datastore_items_data_type import DatastoreItemsDataType


class DeleteAppsDatastoreItemResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.datastore_items_data_type import DatastoreItemsDataType

        return {
            "id": (str,),
            "type": (DatastoreItemsDataType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, type: DatastoreItemsDataType, id: Union[str, UnsetType] = unset, **kwargs):
        """
        Data containing the identifier of the datastore item that was successfully deleted.

        :param id: The unique identifier of the item that was deleted.
        :type id: str, optional

        :param type: The resource type for datastore items.
        :type type: DatastoreItemsDataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
