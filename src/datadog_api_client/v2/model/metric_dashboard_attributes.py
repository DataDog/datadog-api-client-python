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


class MetricDashboardAttributes(ModelNormal):
    validations = {
        "popularity": {
            "inclusive_maximum": 5,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "popularity": (float,),
            "tags": ([str],),
            "title": (str,),
            "url": (str,),
        }

    attribute_map = {
        "popularity": "popularity",
        "tags": "tags",
        "title": "title",
        "url": "url",
    }

    def __init__(
        self_,
        popularity: Union[float, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        url: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes related to the dashboard, including title, popularity, and url.

        :param popularity: Value from 0 to 5 that ranks popularity of the dashboard.
        :type popularity: float, optional

        :param tags: List of tag keys used in the asset.
        :type tags: [str], optional

        :param title: Title of the asset.
        :type title: str, optional

        :param url: URL path of the asset.
        :type url: str, optional
        """
        if popularity is not unset:
            kwargs["popularity"] = popularity
        if tags is not unset:
            kwargs["tags"] = tags
        if title is not unset:
            kwargs["title"] = title
        if url is not unset:
            kwargs["url"] = url
        super().__init__(kwargs)
