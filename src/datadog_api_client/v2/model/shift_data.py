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
    from datadog_api_client.v2.model.shift_data_attributes import ShiftDataAttributes
    from datadog_api_client.v2.model.shift_data_relationships import ShiftDataRelationships
    from datadog_api_client.v2.model.shift_data_type import ShiftDataType


class ShiftData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.shift_data_attributes import ShiftDataAttributes
        from datadog_api_client.v2.model.shift_data_relationships import ShiftDataRelationships
        from datadog_api_client.v2.model.shift_data_type import ShiftDataType

        return {
            "attributes": (ShiftDataAttributes,),
            "id": (str,),
            "relationships": (ShiftDataRelationships,),
            "type": (ShiftDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        type: ShiftDataType,
        attributes: Union[ShiftDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[ShiftDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``ShiftData`` object.

        :param attributes: The definition of ``ShiftDataAttributes`` object.
        :type attributes: ShiftDataAttributes, optional

        :param id: The ``ShiftData`` ``id``.
        :type id: str, optional

        :param relationships: The definition of ``ShiftDataRelationships`` object.
        :type relationships: ShiftDataRelationships, optional

        :param type: Indicates that the resource is of type 'shifts'.
        :type type: ShiftDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
