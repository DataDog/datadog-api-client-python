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


class ExperimentsPublicProtocolResponseDataAttributesAssignmentSourceDefaultPropertiesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "column_name": (str,),
            "column_type": (str,),
            "name": (str,),
        }

    attribute_map = {
        "column_name": "column_name",
        "column_type": "column_type",
        "name": "name",
    }

    def __init__(
        self_,
        column_name: Union[str, UnsetType] = unset,
        column_type: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A default property supplied by the protocol's assignment source.

        :param column_name: Source column that supplies this assignment property.
        :type column_name: str, optional

        :param column_type: Data type of the source column.
        :type column_type: str, optional

        :param name: Display name of the assignment source property.
        :type name: str, optional
        """
        if column_name is not unset:
            kwargs["column_name"] = column_name
        if column_type is not unset:
            kwargs["column_type"] = column_type
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
