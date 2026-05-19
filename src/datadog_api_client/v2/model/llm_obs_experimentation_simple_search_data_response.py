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
    from datadog_api_client.v2.model.llm_obs_experimentation_search_results import LLMObsExperimentationSearchResults
    from datadog_api_client.v2.model.llm_obs_experimentation_type import LLMObsExperimentationType


class LLMObsExperimentationSimpleSearchDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experimentation_search_results import (
            LLMObsExperimentationSearchResults,
        )
        from datadog_api_client.v2.model.llm_obs_experimentation_type import LLMObsExperimentationType

        return {
            "attributes": (LLMObsExperimentationSearchResults,),
            "id": (str,),
            "type": (LLMObsExperimentationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: LLMObsExperimentationSearchResults, id: str, type: LLMObsExperimentationType, **kwargs
    ):
        """
        JSON:API data object for a simple search response.

        :param attributes: The matching experimentation entities grouped by type.
        :type attributes: LLMObsExperimentationSearchResults

        :param id: Server-generated identifier for this search result.
        :type id: str

        :param type: Resource type for experimentation search and analytics operations.
        :type type: LLMObsExperimentationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
