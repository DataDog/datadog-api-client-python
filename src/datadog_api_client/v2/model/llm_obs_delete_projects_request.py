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
    from datadog_api_client.v2.model.llm_obs_delete_projects_data_request import LLMObsDeleteProjectsDataRequest


class LLMObsDeleteProjectsRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_delete_projects_data_request import LLMObsDeleteProjectsDataRequest

        return {
            "data": (LLMObsDeleteProjectsDataRequest,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: LLMObsDeleteProjectsDataRequest, **kwargs):
        """
        Request to delete one or more LLM Observability projects.

        :param data: Data object for deleting LLM Observability projects.
        :type data: LLMObsDeleteProjectsDataRequest
        """
        super().__init__(kwargs)

        self_.data = data
