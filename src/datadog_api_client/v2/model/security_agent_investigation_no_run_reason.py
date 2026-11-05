# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityAgentInvestigationNoRunReason(ModelSimple):
    """
    Why `filter[signal_id]` returned no investigation. Set only on the first page of an empty result. The reason is
        based on the organization's current settings. Poll again only on `investigation_not_started`, after the number
        of seconds in the `Retry-After` header; treat the others as final for this signal.
        - `investigation_not_started`: no investigation has started yet, but one may still start.
        - `not_investigated`: no investigation started within an hour of the signal, so none is expected. The signal
          was skipped for a reason this API doesn't report, such as its severity or a rate limit.
        - `rule_not_enabled`: the signal's detection rule doesn't have Bits Security Analyst enabled, so no
          investigation starts automatically.
        - `signal_not_found`: the ID isn't a signal ID, or no signal with this ID exists in the organization.
        - `org_not_activated`: the organization hasn't activated Bits Security Analyst.

    :param value: Must be one of ["investigation_not_started", "not_investigated", "rule_not_enabled", "signal_not_found", "org_not_activated"].
    :type value: str
    """

    allowed_values = {
        "investigation_not_started",
        "not_investigated",
        "rule_not_enabled",
        "signal_not_found",
        "org_not_activated",
    }
    INVESTIGATION_NOT_STARTED: ClassVar["SecurityAgentInvestigationNoRunReason"]
    NOT_INVESTIGATED: ClassVar["SecurityAgentInvestigationNoRunReason"]
    RULE_NOT_ENABLED: ClassVar["SecurityAgentInvestigationNoRunReason"]
    SIGNAL_NOT_FOUND: ClassVar["SecurityAgentInvestigationNoRunReason"]
    ORG_NOT_ACTIVATED: ClassVar["SecurityAgentInvestigationNoRunReason"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityAgentInvestigationNoRunReason.INVESTIGATION_NOT_STARTED = SecurityAgentInvestigationNoRunReason(
    "investigation_not_started"
)
SecurityAgentInvestigationNoRunReason.NOT_INVESTIGATED = SecurityAgentInvestigationNoRunReason("not_investigated")
SecurityAgentInvestigationNoRunReason.RULE_NOT_ENABLED = SecurityAgentInvestigationNoRunReason("rule_not_enabled")
SecurityAgentInvestigationNoRunReason.SIGNAL_NOT_FOUND = SecurityAgentInvestigationNoRunReason("signal_not_found")
SecurityAgentInvestigationNoRunReason.ORG_NOT_ACTIVATED = SecurityAgentInvestigationNoRunReason("org_not_activated")
