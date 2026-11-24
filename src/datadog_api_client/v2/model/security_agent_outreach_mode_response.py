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
    from datadog_api_client.v2.model.security_agent_outreach_mode_response_data import (
        SecurityAgentOutreachModeResponseData,
    )


class SecurityAgentOutreachModeResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_agent_outreach_mode_response_data import (
            SecurityAgentOutreachModeResponseData,
        )

        return {
            "data": (SecurityAgentOutreachModeResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SecurityAgentOutreachModeResponseData, **kwargs):
        """
        Response with the organization's outreach mode.

        :param data: The organization's outreach mode.
        :type data: SecurityAgentOutreachModeResponseData
        """
        super().__init__(kwargs)

        self_.data = data
