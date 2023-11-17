# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.api_keys_response_meta_page import APIKeysResponseMetaPage


class APIKeysResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.api_keys_response_meta_page import APIKeysResponseMetaPage

        return {
            "max_allowed": (int,),
            "page": (APIKeysResponseMetaPage,),
        }

    attribute_map = {
        "max_allowed": "max_allowed",
        "page": "page",
    }

    def __init__(
        self_,
        max_allowed: Union[int, UnsetType] = unset,
        page: Union[APIKeysResponseMetaPage, UnsetType] = unset,
        **kwargs,
    ):
        """
        Additional information related to api keys response.

        :param max_allowed: Max allowed number of API keys.
        :type max_allowed: int, optional

        :param page: Additional information related to the API keys response.
        :type page: APIKeysResponseMetaPage, optional
        """
        if max_allowed is not unset:
            kwargs["max_allowed"] = max_allowed
        if page is not unset:
            kwargs["page"] = page
        super().__init__(kwargs)
