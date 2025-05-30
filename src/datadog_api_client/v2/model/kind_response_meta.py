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


class KindResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "count": (int,),
        }

    attribute_map = {
        "count": "count",
    }

    def __init__(self_, count: Union[int, UnsetType] = unset, **kwargs):
        """
        Kind response metadata.

        :param count: Total kinds count.
        :type count: int, optional
        """
        if count is not unset:
            kwargs["count"] = count
        super().__init__(kwargs)
