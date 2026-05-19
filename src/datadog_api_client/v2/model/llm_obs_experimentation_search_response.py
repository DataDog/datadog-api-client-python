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
    from datadog_api_client.v2.model.llm_obs_experimentation_search_data_response import (
        LLMObsExperimentationSearchDataResponse,
    )
    from datadog_api_client.v2.model.llm_obs_cursor_meta import LLMObsCursorMeta


class LLMObsExperimentationSearchResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experimentation_search_data_response import (
            LLMObsExperimentationSearchDataResponse,
        )
        from datadog_api_client.v2.model.llm_obs_cursor_meta import LLMObsCursorMeta

        return {
            "data": (LLMObsExperimentationSearchDataResponse,),
            "meta": (LLMObsCursorMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_, data: LLMObsExperimentationSearchDataResponse, meta: Union[LLMObsCursorMeta, UnsetType] = unset, **kwargs
    ):
        """
        Response to a cursor-based experimentation search. Returns ``200 OK`` when all results fit in one page; ``206 Partial Content`` when a next-page cursor is available.

        :param data: JSON:API data object for an experimentation search response.
        :type data: LLMObsExperimentationSearchDataResponse

        :param meta: Pagination cursor metadata.
        :type meta: LLMObsCursorMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
