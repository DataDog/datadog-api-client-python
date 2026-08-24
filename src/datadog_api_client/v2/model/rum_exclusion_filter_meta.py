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


class RumExclusionFilterMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "enabled_at": (int,),
            "updated_at": (int,),
            "updated_by_handle": (str,),
        }

    attribute_map = {
        "enabled_at": "enabled_at",
        "updated_at": "updated_at",
        "updated_by_handle": "updated_by_handle",
    }

    def __init__(
        self_,
        enabled_at: Union[int, UnsetType] = unset,
        updated_at: Union[int, UnsetType] = unset,
        updated_by_handle: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata about the exclusion filter.

        :param enabled_at: Unix epoch (in milliseconds) when the exclusion filter was last enabled.
        :type enabled_at: int, optional

        :param updated_at: Unix epoch (in milliseconds) of the last update.
        :type updated_at: int, optional

        :param updated_by_handle: Handle of the user who last updated the exclusion filter.
        :type updated_by_handle: str, optional
        """
        if enabled_at is not unset:
            kwargs["enabled_at"] = enabled_at
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if updated_by_handle is not unset:
            kwargs["updated_by_handle"] = updated_by_handle
        super().__init__(kwargs)
