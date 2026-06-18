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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ticket_creation_target import TicketCreationTarget


class TicketCreationRuleActionResponse(ModelNormal):
    validations = {
        "max_tickets_per_day": {
            "inclusive_maximum": 500,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ticket_creation_target import TicketCreationTarget

        return {
            "assignee_id": (UUID,),
            "auto_disabled_reason": (str,),
            "fields": (dict,),
            "max_tickets_per_day": (int,),
            "project_id": (UUID,),
            "target": (TicketCreationTarget,),
        }

    attribute_map = {
        "assignee_id": "assignee_id",
        "auto_disabled_reason": "auto_disabled_reason",
        "fields": "fields",
        "max_tickets_per_day": "max_tickets_per_day",
        "project_id": "project_id",
        "target": "target",
    }

    def __init__(
        self_,
        max_tickets_per_day: int,
        project_id: UUID,
        target: TicketCreationTarget,
        assignee_id: Union[UUID, UnsetType] = unset,
        auto_disabled_reason: Union[str, UnsetType] = unset,
        fields: Union[dict, UnsetType] = unset,
        **kwargs,
    ):
        """
        The action to take when the ticket creation rule matches a finding.

        :param assignee_id: The UUID of the default assignee for created tickets.
        :type assignee_id: UUID, optional

        :param auto_disabled_reason: The reason the rule was automatically disabled by the system due to a ticketing integration error.
        :type auto_disabled_reason: str, optional

        :param fields: Custom fields of the Jira issue to create. For the list of available fields, see `Jira documentation <https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issues/#api-rest-api-2-issue-createmeta-projectidorkey-issuetypes-issuetypeid-get>`_.
        :type fields: dict, optional

        :param max_tickets_per_day: The maximum number of tickets the rule may create per day. If exceeded, one final ticket will be created, explaining the limit was hit and link back to the responsible rule.
        :type max_tickets_per_day: int

        :param project_id: The UUID of the case management project.
        :type project_id: UUID

        :param target: The ticketing system to create tickets in.
        :type target: TicketCreationTarget
        """
        if assignee_id is not unset:
            kwargs["assignee_id"] = assignee_id
        if auto_disabled_reason is not unset:
            kwargs["auto_disabled_reason"] = auto_disabled_reason
        if fields is not unset:
            kwargs["fields"] = fields
        super().__init__(kwargs)

        self_.max_tickets_per_day = max_tickets_per_day
        self_.project_id = project_id
        self_.target = target
