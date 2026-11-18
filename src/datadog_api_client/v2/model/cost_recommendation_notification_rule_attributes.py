# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.cost_recommendation_notification_rule_destination_type import (
        CostRecommendationNotificationRuleDestinationType,
    )
    from datadog_api_client.v2.model.cost_recommendation_notification_rule_frequency import (
        CostRecommendationNotificationRuleFrequency,
    )
    from datadog_api_client.v2.model.cost_recommendation_notification_rule_message_customization import (
        CostRecommendationNotificationRuleMessageCustomization,
    )


class CostRecommendationNotificationRuleAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_recommendation_notification_rule_destination_type import (
            CostRecommendationNotificationRuleDestinationType,
        )
        from datadog_api_client.v2.model.cost_recommendation_notification_rule_frequency import (
            CostRecommendationNotificationRuleFrequency,
        )
        from datadog_api_client.v2.model.cost_recommendation_notification_rule_message_customization import (
            CostRecommendationNotificationRuleMessageCustomization,
        )

        return {
            "channel_id": (str,),
            "created_at": (datetime,),
            "created_by": (str,),
            "destination_type": (CostRecommendationNotificationRuleDestinationType,),
            "enabled": (bool,),
            "frequency": (CostRecommendationNotificationRuleFrequency,),
            "interval_execution_date": (str, none_type),
            "interval_execution_time": (str, none_type),
            "mention_targets": ([str],),
            "message_customization": (CostRecommendationNotificationRuleMessageCustomization,),
            "modified_at": (datetime,),
            "modified_by": (str,),
            "name": (str,),
            "org_id": (int,),
            "scope_query": (str,),
            "teams_channel_id": (str,),
            "teams_channel_name": (str,),
            "teams_team_id": (str,),
            "teams_team_name": (str,),
            "teams_tenant_id": (str,),
            "teams_tenant_name": (str,),
            "timezone": (str,),
            "weekly_execution_day": (str, none_type),
            "weekly_execution_time": (str, none_type),
            "workspace_id": (str,),
        }

    attribute_map = {
        "channel_id": "channel_id",
        "created_at": "created_at",
        "created_by": "created_by",
        "destination_type": "destination_type",
        "enabled": "enabled",
        "frequency": "frequency",
        "interval_execution_date": "interval_execution_date",
        "interval_execution_time": "interval_execution_time",
        "mention_targets": "mention_targets",
        "message_customization": "message_customization",
        "modified_at": "modified_at",
        "modified_by": "modified_by",
        "name": "name",
        "org_id": "org_id",
        "scope_query": "scope_query",
        "teams_channel_id": "teams_channel_id",
        "teams_channel_name": "teams_channel_name",
        "teams_team_id": "teams_team_id",
        "teams_team_name": "teams_team_name",
        "teams_tenant_id": "teams_tenant_id",
        "teams_tenant_name": "teams_tenant_name",
        "timezone": "timezone",
        "weekly_execution_day": "weekly_execution_day",
        "weekly_execution_time": "weekly_execution_time",
        "workspace_id": "workspace_id",
    }

    def __init__(
        self_,
        channel_id: str,
        created_at: datetime,
        created_by: str,
        destination_type: CostRecommendationNotificationRuleDestinationType,
        enabled: bool,
        frequency: CostRecommendationNotificationRuleFrequency,
        interval_execution_date: Union[str, none_type],
        interval_execution_time: Union[str, none_type],
        mention_targets: List[str],
        message_customization: CostRecommendationNotificationRuleMessageCustomization,
        modified_at: datetime,
        modified_by: str,
        name: str,
        org_id: int,
        scope_query: str,
        teams_channel_id: str,
        teams_channel_name: str,
        teams_team_id: str,
        teams_team_name: str,
        teams_tenant_id: str,
        teams_tenant_name: str,
        timezone: str,
        weekly_execution_day: Union[str, none_type],
        weekly_execution_time: Union[str, none_type],
        workspace_id: str,
        **kwargs,
    ):
        """
        Attributes of a recommendation notification rule.

        :param channel_id: The Slack channel ID. Empty for ``teams`` rules.
        :type channel_id: str

        :param created_at: When the rule was created.
        :type created_at: datetime

        :param created_by: The UUID of the user who created the rule.
        :type created_by: str

        :param destination_type: Where the digest is sent. ``slack`` requires ``workspace_id`` and ``channel_id`` ; ``teams`` requires the
            ``teams_*`` attributes. Defaults to ``slack``.
        :type destination_type: CostRecommendationNotificationRuleDestinationType

        :param enabled: Whether the digest is sent.
        :type enabled: bool

        :param frequency: How often the digest is sent. ``weekly`` and ``biweekly`` use ``weekly_execution_day`` and ``weekly_execution_time`` ;
            ``every_30`` and ``every_90`` (days) use ``interval_execution_date`` and ``interval_execution_time``.
        :type frequency: CostRecommendationNotificationRuleFrequency

        :param interval_execution_date: The first date ( ``YYYY-MM-DD`` ) of an ``every_30`` or ``every_90`` schedule.
        :type interval_execution_date: str, none_type

        :param interval_execution_time: The time of day ( ``HH:MM`` , in ``timezone`` ) of an ``every_30`` or ``every_90`` schedule.
        :type interval_execution_time: str, none_type

        :param mention_targets: Slack member IDs to mention in the digest. Only valid for ``slack`` rules.
        :type mention_targets: [str]

        :param message_customization: Which sections the digest shows. Sent as a whole: sections left out of a request use their defaults, which
            show everything.
        :type message_customization: CostRecommendationNotificationRuleMessageCustomization

        :param modified_at: When the rule was last modified.
        :type modified_at: datetime

        :param modified_by: The UUID of the user who last modified the rule.
        :type modified_by: str

        :param name: The name of the rule, unique within the organization.
        :type name: str

        :param org_id: The ID of the organization that owns the rule.
        :type org_id: int

        :param scope_query: The recommendation search query that selects what the digest includes. Empty selects every recommendation.
        :type scope_query: str

        :param teams_channel_id: The Microsoft Teams channel ID. Empty for ``slack`` rules.
        :type teams_channel_id: str

        :param teams_channel_name: The Microsoft Teams channel name. Empty for ``slack`` rules.
        :type teams_channel_name: str

        :param teams_team_id: The Microsoft Teams team ID. Empty for ``slack`` rules.
        :type teams_team_id: str

        :param teams_team_name: The Microsoft Teams team name. Empty for ``slack`` rules.
        :type teams_team_name: str

        :param teams_tenant_id: The Microsoft Teams tenant ID. Empty for ``slack`` rules.
        :type teams_tenant_id: str

        :param teams_tenant_name: The Microsoft Teams tenant name. Empty for ``slack`` rules.
        :type teams_tenant_name: str

        :param timezone: The IANA time zone of the schedule.
        :type timezone: str

        :param weekly_execution_day: The day of the week of a ``weekly`` or ``biweekly`` schedule, such as ``monday``.
        :type weekly_execution_day: str, none_type

        :param weekly_execution_time: The time of day ( ``HH:MM`` , in ``timezone`` ) of a ``weekly`` or ``biweekly`` schedule.
        :type weekly_execution_time: str, none_type

        :param workspace_id: The Slack workspace ID. Empty for ``teams`` rules.
        :type workspace_id: str
        """
        super().__init__(kwargs)

        self_.channel_id = channel_id
        self_.created_at = created_at
        self_.created_by = created_by
        self_.destination_type = destination_type
        self_.enabled = enabled
        self_.frequency = frequency
        self_.interval_execution_date = interval_execution_date
        self_.interval_execution_time = interval_execution_time
        self_.mention_targets = mention_targets
        self_.message_customization = message_customization
        self_.modified_at = modified_at
        self_.modified_by = modified_by
        self_.name = name
        self_.org_id = org_id
        self_.scope_query = scope_query
        self_.teams_channel_id = teams_channel_id
        self_.teams_channel_name = teams_channel_name
        self_.teams_team_id = teams_team_id
        self_.teams_team_name = teams_team_name
        self_.teams_tenant_id = teams_tenant_id
        self_.teams_tenant_name = teams_tenant_name
        self_.timezone = timezone
        self_.weekly_execution_day = weekly_execution_day
        self_.weekly_execution_time = weekly_execution_time
        self_.workspace_id = workspace_id
