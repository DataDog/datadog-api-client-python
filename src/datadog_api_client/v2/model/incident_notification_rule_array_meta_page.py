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


class IncidentNotificationRuleArrayMetaPage(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "next_offset": (int,),
            "offset": (int,),
            "size": (int,),
        }

    attribute_map = {
        "next_offset": "next_offset",
        "offset": "offset",
        "size": "size",
    }

    def __init__(
        self_,
        next_offset: Union[int, UnsetType] = unset,
        offset: Union[int, UnsetType] = unset,
        size: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Pagination metadata.

        :param next_offset: The offset for the next page of results.
        :type next_offset: int, optional

        :param offset: The current offset in the results.
        :type offset: int, optional

        :param size: The number of results returned per page.
        :type size: int, optional
        """
        if next_offset is not unset:
            kwargs["next_offset"] = next_offset
        if offset is not unset:
            kwargs["offset"] = offset
        if size is not unset:
            kwargs["size"] = size
        super().__init__(kwargs)
