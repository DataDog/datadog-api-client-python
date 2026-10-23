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
    from datadog_api_client.v2.model.on_call_page_author_relationship import OnCallPageAuthorRelationship
    from datadog_api_client.v2.model.on_call_page_jira_issue_relationship import OnCallPageJiraIssueRelationship
    from datadog_api_client.v2.model.on_call_page_links_relationship import OnCallPageLinksRelationship
    from datadog_api_client.v2.model.on_call_page_responders_relationship import OnCallPageRespondersRelationship
    from datadog_api_client.v2.model.on_call_page_scheduled_action_relationship import (
        OnCallPageScheduledActionRelationship,
    )
    from datadog_api_client.v2.model.on_call_page_service_now_incident_relationship import (
        OnCallPageServiceNowIncidentRelationship,
    )
    from datadog_api_client.v2.model.on_call_page_target_relationship import OnCallPageTargetRelationship
    from datadog_api_client.v2.model.on_call_page_team_routing_rule_relationship import (
        OnCallPageTeamRoutingRuleRelationship,
    )


class OnCallPageDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_page_author_relationship import OnCallPageAuthorRelationship
        from datadog_api_client.v2.model.on_call_page_jira_issue_relationship import OnCallPageJiraIssueRelationship
        from datadog_api_client.v2.model.on_call_page_links_relationship import OnCallPageLinksRelationship
        from datadog_api_client.v2.model.on_call_page_responders_relationship import OnCallPageRespondersRelationship
        from datadog_api_client.v2.model.on_call_page_scheduled_action_relationship import (
            OnCallPageScheduledActionRelationship,
        )
        from datadog_api_client.v2.model.on_call_page_service_now_incident_relationship import (
            OnCallPageServiceNowIncidentRelationship,
        )
        from datadog_api_client.v2.model.on_call_page_target_relationship import OnCallPageTargetRelationship
        from datadog_api_client.v2.model.on_call_page_team_routing_rule_relationship import (
            OnCallPageTeamRoutingRuleRelationship,
        )

        return {
            "author": (OnCallPageAuthorRelationship,),
            "closed_by": (OnCallPageAuthorRelationship,),
            "jira_issue": (OnCallPageJiraIssueRelationship,),
            "links": (OnCallPageLinksRelationship,),
            "responders": (OnCallPageRespondersRelationship,),
            "scheduled_action": (OnCallPageScheduledActionRelationship,),
            "service_now_incident": (OnCallPageServiceNowIncidentRelationship,),
            "target": (OnCallPageTargetRelationship,),
            "team_routing_rule": (OnCallPageTeamRoutingRuleRelationship,),
        }

    attribute_map = {
        "author": "author",
        "closed_by": "closed_by",
        "jira_issue": "jira_issue",
        "links": "links",
        "responders": "responders",
        "scheduled_action": "scheduled_action",
        "service_now_incident": "service_now_incident",
        "target": "target",
        "team_routing_rule": "team_routing_rule",
    }

    def __init__(
        self_,
        author: Union[OnCallPageAuthorRelationship, UnsetType] = unset,
        closed_by: Union[OnCallPageAuthorRelationship, UnsetType] = unset,
        jira_issue: Union[OnCallPageJiraIssueRelationship, UnsetType] = unset,
        links: Union[OnCallPageLinksRelationship, UnsetType] = unset,
        responders: Union[OnCallPageRespondersRelationship, UnsetType] = unset,
        scheduled_action: Union[OnCallPageScheduledActionRelationship, UnsetType] = unset,
        service_now_incident: Union[OnCallPageServiceNowIncidentRelationship, UnsetType] = unset,
        target: Union[OnCallPageTargetRelationship, UnsetType] = unset,
        team_routing_rule: Union[OnCallPageTeamRoutingRuleRelationship, UnsetType] = unset,
        **kwargs,
    ):
        """
        The relationships of an On-Call Page.

        :param author: Reference to the entity that performed an action on the page.
        :type author: OnCallPageAuthorRelationship, optional

        :param closed_by: Reference to the entity that performed an action on the page.
        :type closed_by: OnCallPageAuthorRelationship, optional

        :param jira_issue: The Jira issue linked to the page.
        :type jira_issue: OnCallPageJiraIssueRelationship, optional

        :param links: Links between the page and other Datadog resources, such as incidents. Always empty when listing pages.
        :type links: OnCallPageLinksRelationship, optional

        :param responders: The users responding to the page.
        :type responders: OnCallPageRespondersRelationship, optional

        :param scheduled_action: The next action scheduled on the page, such as an escalation.
        :type scheduled_action: OnCallPageScheduledActionRelationship, optional

        :param service_now_incident: The ServiceNow incident linked to the page.
        :type service_now_incident: OnCallPageServiceNowIncidentRelationship, optional

        :param target: The team, user, or cross-organization handle that was paged.
        :type target: OnCallPageTargetRelationship, optional

        :param team_routing_rule: The team routing rule that matched the page.
        :type team_routing_rule: OnCallPageTeamRoutingRuleRelationship, optional
        """
        if author is not unset:
            kwargs["author"] = author
        if closed_by is not unset:
            kwargs["closed_by"] = closed_by
        if jira_issue is not unset:
            kwargs["jira_issue"] = jira_issue
        if links is not unset:
            kwargs["links"] = links
        if responders is not unset:
            kwargs["responders"] = responders
        if scheduled_action is not unset:
            kwargs["scheduled_action"] = scheduled_action
        if service_now_incident is not unset:
            kwargs["service_now_incident"] = service_now_incident
        if target is not unset:
            kwargs["target"] = target
        if team_routing_rule is not unset:
            kwargs["team_routing_rule"] = team_routing_rule
        super().__init__(kwargs)
