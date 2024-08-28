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


class EntityResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "count": (int,),
            "include_count": (int,),
        }

    attribute_map = {
        "count": "count",
        "include_count": "includeCount",
    }

    def __init__(self_, count: Union[int, UnsetType] = unset, include_count: Union[int, UnsetType] = unset, **kwargs):
        """
        Entity metadata.

        :param count: Total entities count.
        :type count: int, optional

        :param include_count: Total included data count.
        :type include_count: int, optional
        """
        if count is not unset:
            kwargs["count"] = count
        if include_count is not unset:
            kwargs["include_count"] = include_count
        super().__init__(kwargs)
