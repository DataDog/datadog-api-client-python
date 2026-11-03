# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ListConnectionsResponseDataAttributesConnectionsItemsDetailsRefTable(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "table_id": (str,),
            "table_name": (str,),
        }

    attribute_map = {
        "table_id": "table_id",
        "table_name": "table_name",
    }

    def __init__(self_, table_id: Union[str, UnsetType] = unset, table_name: Union[str, UnsetType] = unset, **kwargs):
        """
        Configuration of a reference table connection.

        :param table_id: Identifier of the reference table.
        :type table_id: str, optional

        :param table_name: Name of the reference table.
        :type table_name: str, optional
        """
        if table_id is not unset:
            kwargs["table_id"] = table_id
        if table_name is not unset:
            kwargs["table_name"] = table_name
        super().__init__(kwargs)
