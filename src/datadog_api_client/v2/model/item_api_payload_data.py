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
    from datadog_api_client.v2.model.item_api_payload_data_attributes import ItemApiPayloadDataAttributes
    from datadog_api_client.v2.model.datastore_items_data_type import DatastoreItemsDataType


class ItemApiPayloadData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.item_api_payload_data_attributes import ItemApiPayloadDataAttributes
        from datadog_api_client.v2.model.datastore_items_data_type import DatastoreItemsDataType

        return {
            "attributes": (ItemApiPayloadDataAttributes,),
            "id": (str,),
            "type": (DatastoreItemsDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: DatastoreItemsDataType,
        attributes: Union[ItemApiPayloadDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Core data and metadata for a single datastore item.

        :param attributes: Metadata and content of a datastore item.
        :type attributes: ItemApiPayloadDataAttributes, optional

        :param id: The unique identifier of the datastore.
        :type id: str, optional

        :param type: The resource type for datastore items.
        :type type: DatastoreItemsDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
