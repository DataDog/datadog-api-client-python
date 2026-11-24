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
    from datadog_api_client.v2.model.security_agent_outreach_policy_attributes import (
        SecurityAgentOutreachPolicyAttributes,
    )
    from datadog_api_client.v2.model.security_agent_outreach_policy_type import SecurityAgentOutreachPolicyType


class SecurityAgentOutreachPolicy(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_agent_outreach_policy_attributes import (
            SecurityAgentOutreachPolicyAttributes,
        )
        from datadog_api_client.v2.model.security_agent_outreach_policy_type import SecurityAgentOutreachPolicyType

        return {
            "attributes": (SecurityAgentOutreachPolicyAttributes,),
            "id": (str,),
            "type": (SecurityAgentOutreachPolicyType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityAgentOutreachPolicyAttributes,
        id: str,
        type: SecurityAgentOutreachPolicyType,
        **kwargs,
    ):
        """
        The organization's outreach policy.

        :param attributes: Attributes of the organization's outreach policy.
        :type attributes: SecurityAgentOutreachPolicyAttributes

        :param id: The organization ID.
        :type id: str

        :param type: Type of the outreach policy resource.
        :type type: SecurityAgentOutreachPolicyType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
