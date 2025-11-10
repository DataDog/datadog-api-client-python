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
    from datadog_api_client.v2.model.table_result_v2_data_attributes import TableResultV2DataAttributes
    from datadog_api_client.v2.model.table_result_v2_data_type import TableResultV2DataType


class TableResultV2Data(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.table_result_v2_data_attributes import TableResultV2DataAttributes
        from datadog_api_client.v2.model.table_result_v2_data_type import TableResultV2DataType

        return {
            "attributes": (TableResultV2DataAttributes,),
            "id": (str,),
            "type": (TableResultV2DataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: TableResultV2DataType,
        attributes: Union[TableResultV2DataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The data object containing the reference table configuration and state.

        :param attributes: Attributes that define the reference table's configuration and properties.
        :type attributes: TableResultV2DataAttributes, optional

        :param id: Unique identifier for the reference table.
        :type id: str, optional

        :param type: Reference table resource type.
        :type type: TableResultV2DataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
