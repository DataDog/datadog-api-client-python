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


class MetricAssetAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "title": (str,),
            "url": (str,),
        }

    attribute_map = {
        "title": "title",
        "url": "url",
    }

    def __init__(self_, title: Union[str, UnsetType] = unset, url: Union[str, UnsetType] = unset, **kwargs):
        """
        Assets related to the object, including title and url.

        :param title: Title of the asset.
        :type title: str, optional

        :param url: URL path of the asset.
        :type url: str, optional
        """
        if title is not unset:
            kwargs["title"] = title
        if url is not unset:
            kwargs["url"] = url
        super().__init__(kwargs)
