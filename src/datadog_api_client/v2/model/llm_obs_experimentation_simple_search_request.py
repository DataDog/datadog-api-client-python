# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_experimentation_simple_search_data_request import (
        LLMObsExperimentationSimpleSearchDataRequest,
    )


class LLMObsExperimentationSimpleSearchRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experimentation_simple_search_data_request import (
            LLMObsExperimentationSimpleSearchDataRequest,
        )

        return {
            "data": (LLMObsExperimentationSimpleSearchDataRequest,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: LLMObsExperimentationSimpleSearchDataRequest, **kwargs):
        """
        Request to search across LLM Observability experimentation entities using offset-based pagination.

        :param data: Data object for an experimentation simple search request.
        :type data: LLMObsExperimentationSimpleSearchDataRequest
        """
        super().__init__(kwargs)

        self_.data = data
