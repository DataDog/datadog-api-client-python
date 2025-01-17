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


class HTTPBody(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "content": (str,),
            "content_type": (str,),
        }

    attribute_map = {
        "content": "content",
        "content_type": "content_type",
    }

    def __init__(self_, content: Union[str, UnsetType] = unset, content_type: Union[str, UnsetType] = unset, **kwargs):
        """
        The definition of ``HTTPBody`` object.

        :param content: Serialized body content
        :type content: str, optional

        :param content_type: Content type of the body
        :type content_type: str, optional
        """
        if content is not unset:
            kwargs["content"] = content
        if content_type is not unset:
            kwargs["content_type"] = content_type
        super().__init__(kwargs)
