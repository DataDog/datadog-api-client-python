# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
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


class CostRecommendationNotificationRuleCreateAttributes(ModelNormal):
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
            "destination_type": (CostRecommendationNotificationRuleDestinationType,),
            "enabled": (bool,),
            "frequency": (CostRecommendationNotificationRuleFrequency,),
            "interval_execution_date": (str,),
            "interval_execution_time": (str,),
            "mention_targets": ([str],),
            "message_customization": (CostRecommendationNotificationRuleMessageCustomization,),
            "name": (str,),
            "scope_query": (str,),
            "teams_channel_id": (str,),
            "teams_channel_name": (str,),
            "teams_team_id": (str,),
            "teams_team_name": (str,),
            "teams_tenant_id": (str,),
            "teams_tenant_name": (str,),
            "timezone": (str,),
            "weekly_execution_day": (str,),
            "weekly_execution_time": (str,),
            "workspace_id": (str,),
        }

    attribute_map = {
        "channel_id": "channel_id",
        "destination_type": "destination_type",
        "enabled": "enabled",
        "frequency": "frequency",
        "interval_execution_date": "interval_execution_date",
        "interval_execution_time": "interval_execution_time",
        "mention_targets": "mention_targets",
        "message_customization": "message_customization",
        "name": "name",
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
        frequency: CostRecommendationNotificationRuleFrequency,
        name: str,
        timezone: str,
        channel_id: Union[str, UnsetType] = unset,
        destination_type: Union[CostRecommendationNotificationRuleDestinationType, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        interval_execution_date: Union[str, UnsetType] = unset,
        interval_execution_time: Union[str, UnsetType] = unset,
        mention_targets: Union[List[str], UnsetType] = unset,
        message_customization: Union[CostRecommendationNotificationRuleMessageCustomization, UnsetType] = unset,
        scope_query: Union[str, UnsetType] = unset,
        teams_channel_id: Union[str, UnsetType] = unset,
        teams_channel_name: Union[str, UnsetType] = unset,
        teams_team_id: Union[str, UnsetType] = unset,
        teams_team_name: Union[str, UnsetType] = unset,
        teams_tenant_id: Union[str, UnsetType] = unset,
        teams_tenant_name: Union[str, UnsetType] = unset,
        weekly_execution_day: Union[str, UnsetType] = unset,
        weekly_execution_time: Union[str, UnsetType] = unset,
        workspace_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a new recommendation notification rule. Schedule attributes depend on ``frequency`` and target
        attributes depend on ``destination_type``.

        :param channel_id: The Slack channel ID, starting with ``C`` or ``G``. Required for ``slack`` rules.
        :type channel_id: str, optional

        :param destination_type: Where the digest is sent. ``slack`` requires ``workspace_id`` and ``channel_id`` ; ``teams`` requires the
            ``teams_*`` attributes. Defaults to ``slack``.
        :type destination_type: CostRecommendationNotificationRuleDestinationType, optional

        :param enabled: Whether the digest is sent. Defaults to ``true``.
        :type enabled: bool, optional

        :param frequency: How often the digest is sent. ``weekly`` and ``biweekly`` use ``weekly_execution_day`` and ``weekly_execution_time`` ;
            ``every_30`` and ``every_90`` (days) use ``interval_execution_date`` and ``interval_execution_time``.
        :type frequency: CostRecommendationNotificationRuleFrequency

        :param interval_execution_date: The first date ( ``YYYY-MM-DD`` ) of an ``every_30`` or ``every_90`` schedule.
        :type interval_execution_date: str, optional

        :param interval_execution_time: The time of day ( ``HH:MM`` , in ``timezone`` ) of an ``every_30`` or ``every_90`` schedule.
        :type interval_execution_time: str, optional

        :param mention_targets: Slack member IDs to mention in the digest. Only valid for ``slack`` rules.
        :type mention_targets: [str], optional

        :param message_customization: Which sections the digest shows. Sent as a whole: sections left out of a request use their defaults, which
            show everything.
        :type message_customization: CostRecommendationNotificationRuleMessageCustomization, optional

        :param name: The name of the rule, unique within the organization.
        :type name: str

        :param scope_query: The recommendation search query that selects what the digest includes. Empty selects every recommendation.
        :type scope_query: str, optional

        :param teams_channel_id: The Microsoft Teams channel ID. Required for ``teams`` rules.
        :type teams_channel_id: str, optional

        :param teams_channel_name: The Microsoft Teams channel name. Required for ``teams`` rules.
        :type teams_channel_name: str, optional

        :param teams_team_id: The Microsoft Teams team ID. Required for ``teams`` rules.
        :type teams_team_id: str, optional

        :param teams_team_name: The Microsoft Teams team name. Required for ``teams`` rules.
        :type teams_team_name: str, optional

        :param teams_tenant_id: The Microsoft Teams tenant ID. Required for ``teams`` rules.
        :type teams_tenant_id: str, optional

        :param teams_tenant_name: The Microsoft Teams tenant name. Required for ``teams`` rules.
        :type teams_tenant_name: str, optional

        :param timezone: The IANA time zone of the schedule.
        :type timezone: str

        :param weekly_execution_day: The day of the week of a ``weekly`` or ``biweekly`` schedule, such as ``monday``.
        :type weekly_execution_day: str, optional

        :param weekly_execution_time: The time of day ( ``HH:MM`` , in ``timezone`` ) of a ``weekly`` or ``biweekly`` schedule.
        :type weekly_execution_time: str, optional

        :param workspace_id: The Slack workspace ID, starting with ``T``. Required for ``slack`` rules.
        :type workspace_id: str, optional
        """
        if channel_id is not unset:
            kwargs["channel_id"] = channel_id
        if destination_type is not unset:
            kwargs["destination_type"] = destination_type
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if interval_execution_date is not unset:
            kwargs["interval_execution_date"] = interval_execution_date
        if interval_execution_time is not unset:
            kwargs["interval_execution_time"] = interval_execution_time
        if mention_targets is not unset:
            kwargs["mention_targets"] = mention_targets
        if message_customization is not unset:
            kwargs["message_customization"] = message_customization
        if scope_query is not unset:
            kwargs["scope_query"] = scope_query
        if teams_channel_id is not unset:
            kwargs["teams_channel_id"] = teams_channel_id
        if teams_channel_name is not unset:
            kwargs["teams_channel_name"] = teams_channel_name
        if teams_team_id is not unset:
            kwargs["teams_team_id"] = teams_team_id
        if teams_team_name is not unset:
            kwargs["teams_team_name"] = teams_team_name
        if teams_tenant_id is not unset:
            kwargs["teams_tenant_id"] = teams_tenant_id
        if teams_tenant_name is not unset:
            kwargs["teams_tenant_name"] = teams_tenant_name
        if weekly_execution_day is not unset:
            kwargs["weekly_execution_day"] = weekly_execution_day
        if weekly_execution_time is not unset:
            kwargs["weekly_execution_time"] = weekly_execution_time
        if workspace_id is not unset:
            kwargs["workspace_id"] = workspace_id
        super().__init__(kwargs)

        self_.frequency = frequency
        self_.name = name
        self_.timezone = timezone
