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


class LLMObsSpanSearchOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "include_attachments": (bool,),
            "time_offset": (int,),
        }

    attribute_map = {
        "include_attachments": "include_attachments",
        "time_offset": "time_offset",
    }

    def __init__(
        self_, include_attachments: Union[bool, UnsetType] = unset, time_offset: Union[int, UnsetType] = unset, **kwargs
    ):
        """
        Additional options for a span search request.

        :param include_attachments: Whether to include attachment data in the response. Defaults to ``true``.
        :type include_attachments: bool, optional

        :param time_offset: Offset in seconds applied to both ``from`` and ``to`` timestamps.
        :type time_offset: int, optional
        """
        if include_attachments is not unset:
            kwargs["include_attachments"] = include_attachments
        if time_offset is not unset:
            kwargs["time_offset"] = time_offset
        super().__init__(kwargs)
