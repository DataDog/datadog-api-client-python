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
    from datadog_api_client.v2.model.item_api_payload_data_type import ItemApiPayloadDataType


class ItemApiPayloadData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.item_api_payload_data_attributes import ItemApiPayloadDataAttributes
        from datadog_api_client.v2.model.item_api_payload_data_type import ItemApiPayloadDataType

        return {
            "attributes": (ItemApiPayloadDataAttributes,),
            "id": (str,),
            "type": (ItemApiPayloadDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: ItemApiPayloadDataType,
        attributes: Union[ItemApiPayloadDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``ItemApiPayloadData`` object.

        :param attributes: The definition of ``ItemApiPayloadDataAttributes`` object.
        :type attributes: ItemApiPayloadDataAttributes, optional

        :param id: The ``ItemApiPayloadData`` ``id``.
        :type id: str, optional

        :param type: Items resource type.
        :type type: ItemApiPayloadDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
