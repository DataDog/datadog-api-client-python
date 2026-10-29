# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OnCallPageReleaseOrigin(ModelSimple):
    """
    What snoozed the Page. Only set while the Page is snoozed, together with `release_at`.
        `ack_timeout`: the acknowledgment timeout. `team_rules_active_hours`: the Page was
        triggered outside of the active hours of the team's routing rules. `manual_snooze`:
        a user snoozed the Page.

    :param value: Must be one of ["ack_timeout", "team_rules_active_hours", "manual_snooze"].
    :type value: str
    """

    allowed_values = {
        "ack_timeout",
        "team_rules_active_hours",
        "manual_snooze",
    }
    ACK_TIMEOUT: ClassVar["OnCallPageReleaseOrigin"]
    TEAM_RULES_ACTIVE_HOURS: ClassVar["OnCallPageReleaseOrigin"]
    MANUAL_SNOOZE: ClassVar["OnCallPageReleaseOrigin"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OnCallPageReleaseOrigin.ACK_TIMEOUT = OnCallPageReleaseOrigin("ack_timeout")
OnCallPageReleaseOrigin.TEAM_RULES_ACTIVE_HOURS = OnCallPageReleaseOrigin("team_rules_active_hours")
OnCallPageReleaseOrigin.MANUAL_SNOOZE = OnCallPageReleaseOrigin("manual_snooze")
