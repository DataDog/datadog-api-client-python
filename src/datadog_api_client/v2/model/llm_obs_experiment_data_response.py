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
    from datadog_api_client.v2.model.llm_obs_experiment_data_attributes_response import (
        LLMObsExperimentDataAttributesResponse,
    )
    from datadog_api_client.v2.model.llm_obs_experiment_type import LLMObsExperimentType


class LLMObsExperimentDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experiment_data_attributes_response import (
            LLMObsExperimentDataAttributesResponse,
        )
        from datadog_api_client.v2.model.llm_obs_experiment_type import LLMObsExperimentType

        return {
            "attributes": (LLMObsExperimentDataAttributesResponse,),
            "id": (str,),
            "type": (LLMObsExperimentType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: LLMObsExperimentDataAttributesResponse, id: str, type: LLMObsExperimentType, **kwargs
    ):
        """
        Data object for an LLM Observability experiment.

        :param attributes: Attributes of an LLM Observability experiment.
        :type attributes: LLMObsExperimentDataAttributesResponse

        :param id: Unique identifier of the experiment.
        :type id: str

        :param type: Resource type of an LLM Observability experiment.
        :type type: LLMObsExperimentType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
