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
    from datadog_api_client.v2.model.security_agent_outreach_rules_update_request_data import (
        SecurityAgentOutreachRulesUpdateRequestData,
    )


class SecurityAgentOutreachRulesUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_agent_outreach_rules_update_request_data import (
            SecurityAgentOutreachRulesUpdateRequestData,
        )

        return {
            "data": (SecurityAgentOutreachRulesUpdateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SecurityAgentOutreachRulesUpdateRequestData, **kwargs):
        """
        Request to upsert the outreach automation state of detection rules.

        :param data: The rules to upsert.
        :type data: SecurityAgentOutreachRulesUpdateRequestData
        """
        super().__init__(kwargs)

        self_.data = data
