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
    from datadog_api_client.v2.model.security_agent_investigation_data import SecurityAgentInvestigationData


class SecurityAgentInvestigationResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_agent_investigation_data import SecurityAgentInvestigationData

        return {
            "data": (SecurityAgentInvestigationData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SecurityAgentInvestigationData, **kwargs):
        """
        An investigation.

        :param data: An investigation and its content. ``attributes`` is absent when ``fields[investigations]`` is empty or lists
            only attributes the investigation doesn't have.
        :type data: SecurityAgentInvestigationData
        """
        super().__init__(kwargs)

        self_.data = data
