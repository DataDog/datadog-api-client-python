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
    from datadog_api_client.v2.model.table_row_resource_data_attributes import TableRowResourceDataAttributes
    from datadog_api_client.v2.model.table_row_resource_data_type import TableRowResourceDataType


class TableRowResourceData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.table_row_resource_data_attributes import TableRowResourceDataAttributes
        from datadog_api_client.v2.model.table_row_resource_data_type import TableRowResourceDataType

        return {
            "attributes": (TableRowResourceDataAttributes,),
            "id": (str,),
            "type": (TableRowResourceDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: TableRowResourceDataType,
        attributes: Union[TableRowResourceDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the table row resource data object.

        :param attributes: The definition of the row attributes object.
        :type attributes: TableRowResourceDataAttributes, optional

        :param id: The ID of the row.
        :type id: str, optional

        :param type: Row resource type.
        :type type: TableRowResourceDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
