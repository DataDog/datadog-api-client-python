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
    from datadog_api_client.v2.model.llm_obs_span_data import LLMObsSpanData
    from datadog_api_client.v2.model.llm_obs_spans_response_links import LLMObsSpansResponseLinks
    from datadog_api_client.v2.model.llm_obs_spans_response_meta import LLMObsSpansResponseMeta


class LLMObsSpansResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_span_data import LLMObsSpanData
        from datadog_api_client.v2.model.llm_obs_spans_response_links import LLMObsSpansResponseLinks
        from datadog_api_client.v2.model.llm_obs_spans_response_meta import LLMObsSpansResponseMeta

        return {
            "data": ([LLMObsSpanData],),
            "links": (LLMObsSpansResponseLinks,),
            "meta": (LLMObsSpansResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[LLMObsSpanData],
        meta: LLMObsSpansResponseMeta,
        links: Union[LLMObsSpansResponseLinks, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing a list of LLM Observability spans.

        :param data: List of spans matching the query.
        :type data: [LLMObsSpanData]

        :param links: Pagination links accompanying the spans response.
        :type links: LLMObsSpansResponseLinks, optional

        :param meta: Metadata accompanying the spans response.
        :type meta: LLMObsSpansResponseMeta
        """
        if links is not unset:
            kwargs["links"] = links
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
