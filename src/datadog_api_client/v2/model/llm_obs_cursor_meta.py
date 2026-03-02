# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class LLMObsCursorMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "after": (str, none_type),
        }

    attribute_map = {
        "after": "after",
    }

    def __init__(self_, after: Union[str, none_type, UnsetType] = unset, **kwargs):
        """
        Pagination cursor metadata.

        :param after: Cursor for the next page of results.
        :type after: str, none_type, optional
        """
        if after is not unset:
            kwargs["after"] = after
        super().__init__(kwargs)
