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


class HostMapWidgetGroupBy(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "column": (str,),
            "key": (str,),
        }

    attribute_map = {
        "column": "column",
        "key": "key",
    }

    def __init__(self_, column: str, key: Union[str, UnsetType] = unset, **kwargs):
        """
        Defines a grouping dimension for the infrastructure host map.

        :param column: Column name from the entity table (for example, ``cloud_provider`` , ``tags`` , ``labels`` ).
        :type column: str

        :param key: Key within the column for nested attribute types (for example, ``service`` within ``tags`` ).
        :type key: str, optional
        """
        if key is not unset:
            kwargs["key"] = key
        super().__init__(kwargs)

        self_.column = column
