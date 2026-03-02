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
    from datadog_api_client.v2.model.llm_obs_project_data_attributes_response import LLMObsProjectDataAttributesResponse
    from datadog_api_client.v2.model.llm_obs_project_type import LLMObsProjectType


class LLMObsProjectDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_project_data_attributes_response import (
            LLMObsProjectDataAttributesResponse,
        )
        from datadog_api_client.v2.model.llm_obs_project_type import LLMObsProjectType

        return {
            "attributes": (LLMObsProjectDataAttributesResponse,),
            "id": (str,),
            "type": (LLMObsProjectType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: LLMObsProjectDataAttributesResponse, id: str, type: LLMObsProjectType, **kwargs):
        """
        Data object for an LLM Observability project.

        :param attributes: Attributes of an LLM Observability project.
        :type attributes: LLMObsProjectDataAttributesResponse

        :param id: Unique identifier of the project.
        :type id: str

        :param type: Resource type of an LLM Observability project.
        :type type: LLMObsProjectType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
