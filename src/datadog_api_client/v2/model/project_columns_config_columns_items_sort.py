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


class ProjectColumnsConfigColumnsItemsSort(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "ascending": (bool,),
            "priority": (int,),
        }

    attribute_map = {
        "ascending": "ascending",
        "priority": "priority",
    }

    def __init__(self_, ascending: Union[bool, UnsetType] = unset, priority: Union[int, UnsetType] = unset, **kwargs):
        """


        :param ascending:
        :type ascending: bool, optional

        :param priority:
        :type priority: int, optional
        """
        if ascending is not unset:
            kwargs["ascending"] = ascending
        if priority is not unset:
            kwargs["priority"] = priority
        super().__init__(kwargs)
