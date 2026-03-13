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


class RumSegmentJourney(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "conversion_type": (str,),
            "group_by": (str,),
            "name": (str,),
            "search": (str,),
        }

    attribute_map = {
        "conversion_type": "conversion_type",
        "group_by": "group_by",
        "name": "name",
        "search": "search",
    }

    def __init__(
        self_,
        conversion_type: Union[str, UnsetType] = unset,
        group_by: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        search: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A journey-based query block within a segment data query.

        :param conversion_type: The type of conversion to track.
        :type conversion_type: str, optional

        :param group_by: The facet to group journey results by.
        :type group_by: str, optional

        :param name: The name of this journey query block.
        :type name: str, optional

        :param search: The search query for filtering events.
        :type search: str, optional
        """
        if conversion_type is not unset:
            kwargs["conversion_type"] = conversion_type
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if name is not unset:
            kwargs["name"] = name
        if search is not unset:
            kwargs["search"] = search
        super().__init__(kwargs)
