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
    from datadog_api_client.v2.model.security_agent_outreach_mode_attributes import SecurityAgentOutreachModeAttributes
    from datadog_api_client.v2.model.security_agent_outreach_policy_type import SecurityAgentOutreachPolicyType


class SecurityAgentOutreachModeResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_agent_outreach_mode_attributes import (
            SecurityAgentOutreachModeAttributes,
        )
        from datadog_api_client.v2.model.security_agent_outreach_policy_type import SecurityAgentOutreachPolicyType

        return {
            "attributes": (SecurityAgentOutreachModeAttributes,),
            "id": (str,),
            "type": (SecurityAgentOutreachPolicyType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: SecurityAgentOutreachModeAttributes, id: str, type: SecurityAgentOutreachPolicyType, **kwargs
    ):
        """
        The organization's outreach mode.

        :param attributes: Attributes of a mode-only policy update.
        :type attributes: SecurityAgentOutreachModeAttributes

        :param id: The organization ID.
        :type id: str

        :param type: Type of the outreach policy resource.
        :type type: SecurityAgentOutreachPolicyType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
