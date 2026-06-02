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


class StatuspageUrlSettingUpdateAttributes(ModelNormal):
    validations = {
        "custom_tags": {
            "min_length": 1,
        },
        "url": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "custom_tags": (str,),
            "url": (str,),
        }

    attribute_map = {
        "custom_tags": "custom_tags",
        "url": "url",
    }

    def __init__(self_, custom_tags: Union[str, UnsetType] = unset, url: Union[str, UnsetType] = unset, **kwargs):
        """
        The Statuspage URL setting attributes for an update request.

        :param custom_tags: Comma-separated list of custom tags to apply to events generated from this Statuspage URL.
        :type custom_tags: str, optional

        :param url: The Statuspage URL to monitor.
        :type url: str, optional
        """
        if custom_tags is not unset:
            kwargs["custom_tags"] = custom_tags
        if url is not unset:
            kwargs["url"] = url
        super().__init__(kwargs)
