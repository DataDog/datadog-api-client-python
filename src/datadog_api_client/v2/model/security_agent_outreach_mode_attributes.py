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
    from datadog_api_client.v2.model.security_agent_outreach_mode import SecurityAgentOutreachMode


class SecurityAgentOutreachModeAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_agent_outreach_mode import SecurityAgentOutreachMode

        return {
            "mode": (SecurityAgentOutreachMode,),
        }

    attribute_map = {
        "mode": "mode",
    }

    def __init__(self_, mode: SecurityAgentOutreachMode, **kwargs):
        """
        Attributes of a mode-only policy update.

        :param mode: The organization's outreach mode. ``off`` disables user outreach. ``manual`` only sends outreach an analyst
            triggers. ``automated`` auto-sends automated interviews for rules with outreach enabled, to users whose email
            domain is allowed.
        :type mode: SecurityAgentOutreachMode
        """
        super().__init__(kwargs)

        self_.mode = mode
