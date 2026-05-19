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
    from datadog_api_client.v2.model.llm_obs_experimentation_search_data_request import (
        LLMObsExperimentationSearchDataRequest,
    )


class LLMObsExperimentationSearchRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experimentation_search_data_request import (
            LLMObsExperimentationSearchDataRequest,
        )

        return {
            "data": (LLMObsExperimentationSearchDataRequest,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: LLMObsExperimentationSearchDataRequest, **kwargs):
        """
        Request to search across LLM Observability experimentation entities using cursor-based pagination.

        :param data: Data object for an experimentation search request.
        :type data: LLMObsExperimentationSearchDataRequest
        """
        super().__init__(kwargs)

        self_.data = data
