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


class RecommendationsPageMetaPage(ModelNormal):
    validations = {
        "page_size": {
            "inclusive_maximum": 10000,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "filter": (str,),
            "next_page_token": (str,),
            "page_size": (int,),
            "page_token": (str,),
        }

    attribute_map = {
        "filter": "filter",
        "next_page_token": "next_page_token",
        "page_size": "page_size",
        "page_token": "page_token",
    }

    def __init__(
        self_,
        filter: Union[str, UnsetType] = unset,
        next_page_token: Union[str, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        page_token: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Pagination metadata for a page of cost recommendations.

        :param filter: The filter expression that was applied to produce this page.
        :type filter: str, optional

        :param next_page_token: Opaque token used to fetch the next page; absent on the last page.
        :type next_page_token: str, optional

        :param page_size: Number of items returned in this page (1–10000).
        :type page_size: int, optional

        :param page_token: Pagination token echoed back from the request.
        :type page_token: str, optional
        """
        if filter is not unset:
            kwargs["filter"] = filter
        if next_page_token is not unset:
            kwargs["next_page_token"] = next_page_token
        if page_size is not unset:
            kwargs["page_size"] = page_size
        if page_token is not unset:
            kwargs["page_token"] = page_token
        super().__init__(kwargs)
