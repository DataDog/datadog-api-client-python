# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.span import Span
    from datadog_api_client.v2.model.spans_list_response_links import SpansListResponseLinks
    from datadog_api_client.v2.model.spans_list_response_metadata import SpansListResponseMetadata


class SpansListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.span import Span
        from datadog_api_client.v2.model.spans_list_response_links import SpansListResponseLinks
        from datadog_api_client.v2.model.spans_list_response_metadata import SpansListResponseMetadata

        return {
            "data": ([Span],),
            "links": (SpansListResponseLinks,),
            "meta": (SpansListResponseMetadata,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[Span], UnsetType] = unset,
        links: Union[SpansListResponseLinks, UnsetType] = unset,
        meta: Union[SpansListResponseMetadata, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response object with all spans matching the request and pagination information.

        :param data: Array of spans matching the request.
        :type data: [Span], optional

        :param links: Links attributes.
        :type links: SpansListResponseLinks, optional

        :param meta: The metadata associated with a request.
        :type meta: SpansListResponseMetadata, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if links is not unset:
            kwargs["links"] = links
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
