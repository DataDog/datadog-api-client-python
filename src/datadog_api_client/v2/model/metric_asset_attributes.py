# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

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
            "tags": ([str],),
            "title": (str,),
            "url": (str,),
        }

    attribute_map = {
        "tags": "tags",
        "title": "title",
        "url": "url",
    }

    def __init__(
        self_,
        tags: Union[List[str], UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        url: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Assets related to the object, including title, url, and tags.

        :param tags: List of tag keys used in the asset.
        :type tags: [str], optional

        :param title: Title of the asset.
        :type title: str, optional

        :param url: URL path of the asset.
        :type url: str, optional
        """
        if tags is not unset:
            kwargs["tags"] = tags
        if title is not unset:
            kwargs["title"] = title
        if url is not unset:
            kwargs["url"] = url
        super().__init__(kwargs)
