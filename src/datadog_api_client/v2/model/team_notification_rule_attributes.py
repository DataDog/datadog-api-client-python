# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.team_notification_rule_attributes_email import TeamNotificationRuleAttributesEmail
    from datadog_api_client.v2.model.team_notification_rule_attributes_ms_teams import (
        TeamNotificationRuleAttributesMsTeams,
    )
    from datadog_api_client.v2.model.team_notification_rule_attributes_pagerduty import (
        TeamNotificationRuleAttributesPagerduty,
    )
    from datadog_api_client.v2.model.team_notification_rule_attributes_slack import TeamNotificationRuleAttributesSlack


class TeamNotificationRuleAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_notification_rule_attributes_email import (
            TeamNotificationRuleAttributesEmail,
        )
        from datadog_api_client.v2.model.team_notification_rule_attributes_ms_teams import (
            TeamNotificationRuleAttributesMsTeams,
        )
        from datadog_api_client.v2.model.team_notification_rule_attributes_pagerduty import (
            TeamNotificationRuleAttributesPagerduty,
        )
        from datadog_api_client.v2.model.team_notification_rule_attributes_slack import (
            TeamNotificationRuleAttributesSlack,
        )

        return {
            "email": (TeamNotificationRuleAttributesEmail,),
            "ms_teams": (TeamNotificationRuleAttributesMsTeams,),
            "pagerduty": (TeamNotificationRuleAttributesPagerduty,),
            "slack": (TeamNotificationRuleAttributesSlack,),
        }

    attribute_map = {
        "email": "email",
        "ms_teams": "ms_teams",
        "pagerduty": "pagerduty",
        "slack": "slack",
    }

    def __init__(
        self_,
        email: Union[TeamNotificationRuleAttributesEmail, UnsetType] = unset,
        ms_teams: Union[TeamNotificationRuleAttributesMsTeams, UnsetType] = unset,
        pagerduty: Union[TeamNotificationRuleAttributesPagerduty, UnsetType] = unset,
        slack: Union[TeamNotificationRuleAttributesSlack, UnsetType] = unset,
        **kwargs,
    ):
        """
        Team notification rule attributes

        :param email: Email notification settings for the team
        :type email: TeamNotificationRuleAttributesEmail, optional

        :param ms_teams: MS Teams notification settings for the team
        :type ms_teams: TeamNotificationRuleAttributesMsTeams, optional

        :param pagerduty: PagerDuty notification settings for the team
        :type pagerduty: TeamNotificationRuleAttributesPagerduty, optional

        :param slack: Slack notification settings for the team
        :type slack: TeamNotificationRuleAttributesSlack, optional
        """
        if email is not unset:
            kwargs["email"] = email
        if ms_teams is not unset:
            kwargs["ms_teams"] = ms_teams
        if pagerduty is not unset:
            kwargs["pagerduty"] = pagerduty
        if slack is not unset:
            kwargs["slack"] = slack
        super().__init__(kwargs)
