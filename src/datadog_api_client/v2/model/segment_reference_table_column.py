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


class SegmentReferenceTableColumn(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "alias": (str,),
            "name": (str,),
        }

    attribute_map = {
        "alias": "alias",
        "name": "name",
    }

    def __init__(self_, alias: Union[str, UnsetType] = unset, name: Union[str, UnsetType] = unset, **kwargs):
        """
        A reference table column to include.

        :param alias: Name to use for the column.
        :type alias: str, optional

        :param name: Name of the column in the reference table.
        :type name: str, optional
        """
        if alias is not unset:
            kwargs["alias"] = alias
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
