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
    from datadog_api_client.v2.model.security_agent_investigation_create_attributes import (
        SecurityAgentInvestigationCreateAttributes,
    )
    from datadog_api_client.v2.model.security_agent_investigation_type import SecurityAgentInvestigationType


class SecurityAgentInvestigationCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_agent_investigation_create_attributes import (
            SecurityAgentInvestigationCreateAttributes,
        )
        from datadog_api_client.v2.model.security_agent_investigation_type import SecurityAgentInvestigationType

        return {
            "attributes": (SecurityAgentInvestigationCreateAttributes,),
            "type": (SecurityAgentInvestigationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: SecurityAgentInvestigationCreateAttributes, type: SecurityAgentInvestigationType, **kwargs
    ):
        """
        The investigation to start.

        :param attributes: Attributes of the investigation to start.
        :type attributes: SecurityAgentInvestigationCreateAttributes

        :param type: Type of the investigation resource.
        :type type: SecurityAgentInvestigationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
