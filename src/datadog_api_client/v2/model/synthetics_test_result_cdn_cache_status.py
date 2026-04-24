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


class SyntheticsTestResultCdnCacheStatus(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "cached": (bool,),
            "status": (str,),
        }

    attribute_map = {
        "cached": "cached",
        "status": "status",
    }

    def __init__(self_, cached: Union[bool, UnsetType] = unset, status: Union[str, UnsetType] = unset, **kwargs):
        """
        Cache status reported by the CDN for the response.

        :param cached: Whether the response was served from the CDN cache.
        :type cached: bool, optional

        :param status: Raw cache status string reported by the CDN.
        :type status: str, optional
        """
        if cached is not unset:
            kwargs["cached"] = cached
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)
