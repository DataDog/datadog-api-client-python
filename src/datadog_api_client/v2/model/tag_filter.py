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


class TagFilter(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "tag_key": (str,),
            "tag_value": (str,),
        }

    attribute_map = {
        "tag_key": "tag_key",
        "tag_value": "tag_value",
    }

    def __init__(self_, tag_key: Union[str, UnsetType] = unset, tag_value: Union[str, UnsetType] = unset, **kwargs):
        """
        Tag filter for the budget's entries.

        :param tag_key: The key of the tag.
        :type tag_key: str, optional

        :param tag_value: The value of the tag.
        :type tag_value: str, optional
        """
        if tag_key is not unset:
            kwargs["tag_key"] = tag_key
        if tag_value is not unset:
            kwargs["tag_value"] = tag_value
        super().__init__(kwargs)
