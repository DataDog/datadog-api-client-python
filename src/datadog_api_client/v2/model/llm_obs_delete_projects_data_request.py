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
    from datadog_api_client.v2.model.llm_obs_delete_projects_data_attributes_request import (
        LLMObsDeleteProjectsDataAttributesRequest,
    )
    from datadog_api_client.v2.model.llm_obs_project_type import LLMObsProjectType


class LLMObsDeleteProjectsDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_delete_projects_data_attributes_request import (
            LLMObsDeleteProjectsDataAttributesRequest,
        )
        from datadog_api_client.v2.model.llm_obs_project_type import LLMObsProjectType

        return {
            "attributes": (LLMObsDeleteProjectsDataAttributesRequest,),
            "type": (LLMObsProjectType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: LLMObsDeleteProjectsDataAttributesRequest, type: LLMObsProjectType, **kwargs):
        """
        Data object for deleting LLM Observability projects.

        :param attributes: Attributes for deleting LLM Observability projects.
        :type attributes: LLMObsDeleteProjectsDataAttributesRequest

        :param type: Resource type of an LLM Observability project.
        :type type: LLMObsProjectType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
