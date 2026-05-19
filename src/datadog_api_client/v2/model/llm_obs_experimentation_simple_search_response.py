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
    from datadog_api_client.v2.model.llm_obs_experimentation_simple_search_data_response import (
        LLMObsExperimentationSimpleSearchDataResponse,
    )
    from datadog_api_client.v2.model.llm_obs_experimentation_simple_search_meta import (
        LLMObsExperimentationSimpleSearchMeta,
    )


class LLMObsExperimentationSimpleSearchResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experimentation_simple_search_data_response import (
            LLMObsExperimentationSimpleSearchDataResponse,
        )
        from datadog_api_client.v2.model.llm_obs_experimentation_simple_search_meta import (
            LLMObsExperimentationSimpleSearchMeta,
        )

        return {
            "data": (LLMObsExperimentationSimpleSearchDataResponse,),
            "meta": (LLMObsExperimentationSimpleSearchMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: LLMObsExperimentationSimpleSearchDataResponse,
        meta: Union[LLMObsExperimentationSimpleSearchMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response to an offset-based experimentation simple search.

        :param data: JSON:API data object for a simple search response.
        :type data: LLMObsExperimentationSimpleSearchDataResponse

        :param meta: Pagination metadata for a simple search response.
        :type meta: LLMObsExperimentationSimpleSearchMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
