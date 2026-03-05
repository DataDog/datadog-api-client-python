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
    from datadog_api_client.v2.model.llm_obs_experiment_data_attributes_request import (
        LLMObsExperimentDataAttributesRequest,
    )
    from datadog_api_client.v2.model.llm_obs_experiment_type import LLMObsExperimentType


class LLMObsExperimentDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experiment_data_attributes_request import (
            LLMObsExperimentDataAttributesRequest,
        )
        from datadog_api_client.v2.model.llm_obs_experiment_type import LLMObsExperimentType

        return {
            "attributes": (LLMObsExperimentDataAttributesRequest,),
            "type": (LLMObsExperimentType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: LLMObsExperimentDataAttributesRequest, type: LLMObsExperimentType, **kwargs):
        """
        Data object for creating an LLM Observability experiment.

        :param attributes: Attributes for creating an LLM Observability experiment.
        :type attributes: LLMObsExperimentDataAttributesRequest

        :param type: Resource type of an LLM Observability experiment.
        :type type: LLMObsExperimentType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
