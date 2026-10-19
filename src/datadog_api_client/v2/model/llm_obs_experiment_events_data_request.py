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
    from datadog_api_client.v2.model.llm_obs_experiment_events_data_attributes_request import (
        LLMObsExperimentEventsDataAttributesRequest,
    )
    from datadog_api_client.v2.model.llm_obs_experiment_type import LLMObsExperimentType


class LLMObsExperimentEventsDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experiment_events_data_attributes_request import (
            LLMObsExperimentEventsDataAttributesRequest,
        )
        from datadog_api_client.v2.model.llm_obs_experiment_type import LLMObsExperimentType

        return {
            "attributes": (LLMObsExperimentEventsDataAttributesRequest,),
            "type": (LLMObsExperimentType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: LLMObsExperimentEventsDataAttributesRequest, type: LLMObsExperimentType, **kwargs):
        """
        Data object for pushing experiment events.

        :param attributes: Attributes for pushing experiment events including spans and metrics.
        :type attributes: LLMObsExperimentEventsDataAttributesRequest

        :param type: Resource type of an Agent Observability experiment.
        :type type: LLMObsExperimentType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
