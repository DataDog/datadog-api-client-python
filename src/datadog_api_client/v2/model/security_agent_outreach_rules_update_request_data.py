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
    from datadog_api_client.v2.model.security_agent_outreach_rules_update_attributes import (
        SecurityAgentOutreachRulesUpdateAttributes,
    )
    from datadog_api_client.v2.model.security_agent_outreach_rules_update_type import (
        SecurityAgentOutreachRulesUpdateType,
    )


class SecurityAgentOutreachRulesUpdateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_agent_outreach_rules_update_attributes import (
            SecurityAgentOutreachRulesUpdateAttributes,
        )
        from datadog_api_client.v2.model.security_agent_outreach_rules_update_type import (
            SecurityAgentOutreachRulesUpdateType,
        )

        return {
            "attributes": (SecurityAgentOutreachRulesUpdateAttributes,),
            "type": (SecurityAgentOutreachRulesUpdateType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityAgentOutreachRulesUpdateAttributes,
        type: SecurityAgentOutreachRulesUpdateType,
        **kwargs,
    ):
        """
        The rules to upsert.

        :param attributes: Attributes of an outreach policy rules update request.
        :type attributes: SecurityAgentOutreachRulesUpdateAttributes

        :param type: Type of an outreach policy rules update request.
        :type type: SecurityAgentOutreachRulesUpdateType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
