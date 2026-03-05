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
    from datadog_api_client.v2.model.llm_obs_project_update_data_attributes_request import (
        LLMObsProjectUpdateDataAttributesRequest,
    )
    from datadog_api_client.v2.model.llm_obs_project_type import LLMObsProjectType


class LLMObsProjectUpdateDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_project_update_data_attributes_request import (
            LLMObsProjectUpdateDataAttributesRequest,
        )
        from datadog_api_client.v2.model.llm_obs_project_type import LLMObsProjectType

        return {
            "attributes": (LLMObsProjectUpdateDataAttributesRequest,),
            "type": (LLMObsProjectType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: LLMObsProjectUpdateDataAttributesRequest, type: LLMObsProjectType, **kwargs):
        """
        Data object for updating an LLM Observability project.

        :param attributes: Attributes for updating an LLM Observability project.
        :type attributes: LLMObsProjectUpdateDataAttributesRequest

        :param type: Resource type of an LLM Observability project.
        :type type: LLMObsProjectType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
