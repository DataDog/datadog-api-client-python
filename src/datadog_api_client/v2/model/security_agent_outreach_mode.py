# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityAgentOutreachMode(ModelSimple):
    """
    The organization's outreach mode. `off` disables user outreach. `manual` only sends outreach an analyst
        triggers. `automated` auto-sends automated interviews for rules with outreach enabled, to users whose email
        domain is allowed.

    :param value: Must be one of ["off", "manual", "automated"].
    :type value: str
    """

    allowed_values = {
        "off",
        "manual",
        "automated",
    }
    OFF: ClassVar["SecurityAgentOutreachMode"]
    MANUAL: ClassVar["SecurityAgentOutreachMode"]
    AUTOMATED: ClassVar["SecurityAgentOutreachMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityAgentOutreachMode.OFF = SecurityAgentOutreachMode("off")
SecurityAgentOutreachMode.MANUAL = SecurityAgentOutreachMode("manual")
SecurityAgentOutreachMode.AUTOMATED = SecurityAgentOutreachMode("automated")
