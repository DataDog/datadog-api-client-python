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
    from datadog_api_client.v2.model.llm_obs_experiment_events_v2_data_attributes_response import (
        LLMObsExperimentEventsV2DataAttributesResponse,
    )
    from datadog_api_client.v2.model.llm_obs_experiment_events_type import LLMObsExperimentEventsType


class LLMObsExperimentEventsV2DataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experiment_events_v2_data_attributes_response import (
            LLMObsExperimentEventsV2DataAttributesResponse,
        )
        from datadog_api_client.v2.model.llm_obs_experiment_events_type import LLMObsExperimentEventsType

        return {
            "attributes": (LLMObsExperimentEventsV2DataAttributesResponse,),
            "id": (str,),
            "type": (LLMObsExperimentEventsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: LLMObsExperimentEventsV2DataAttributesResponse,
        id: str,
        type: LLMObsExperimentEventsType,
        **kwargs,
    ):
        """
        JSON:API data object for an experiment events response.

        :param attributes: Attributes of an experiment events response.
        :type attributes: LLMObsExperimentEventsV2DataAttributesResponse

        :param id: Identifier for this events resource.
        :type id: str

        :param type: Resource type for an experiment events collection.
        :type type: LLMObsExperimentEventsType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
