# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.jira_issue import JiraIssue
    from datadog_api_client.v2.model.case_priority import CasePriority
    from datadog_api_client.v2.model.service_now_ticket import ServiceNowTicket
    from datadog_api_client.v2.model.case_status import CaseStatus
    from datadog_api_client.v2.model.case_type import CaseType


class CaseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.jira_issue import JiraIssue
        from datadog_api_client.v2.model.case_priority import CasePriority
        from datadog_api_client.v2.model.service_now_ticket import ServiceNowTicket
        from datadog_api_client.v2.model.case_status import CaseStatus
        from datadog_api_client.v2.model.case_type import CaseType

        return {
            "archived_at": (datetime, none_type),
            "closed_at": (datetime, none_type),
            "created_at": (datetime,),
            "description": (str,),
            "jira_issue": (JiraIssue,),
            "key": (str,),
            "modified_at": (datetime, none_type),
            "priority": (CasePriority,),
            "service_now_ticket": (ServiceNowTicket,),
            "status": (CaseStatus,),
            "title": (str,),
            "type": (CaseType,),
        }

    attribute_map = {
        "archived_at": "archived_at",
        "closed_at": "closed_at",
        "created_at": "created_at",
        "description": "description",
        "jira_issue": "jira_issue",
        "key": "key",
        "modified_at": "modified_at",
        "priority": "priority",
        "service_now_ticket": "service_now_ticket",
        "status": "status",
        "title": "title",
        "type": "type",
    }
    read_only_vars = {
        "archived_at",
        "closed_at",
        "created_at",
        "jira_issue",
        "modified_at",
        "service_now_ticket",
    }

    def __init__(
        self_,
        archived_at: Union[datetime, none_type, UnsetType] = unset,
        closed_at: Union[datetime, none_type, UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        jira_issue: Union[JiraIssue, none_type, UnsetType] = unset,
        key: Union[str, UnsetType] = unset,
        modified_at: Union[datetime, none_type, UnsetType] = unset,
        priority: Union[CasePriority, UnsetType] = unset,
        service_now_ticket: Union[ServiceNowTicket, none_type, UnsetType] = unset,
        status: Union[CaseStatus, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        type: Union[CaseType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Case attributes

        :param archived_at: Timestamp of when the case was archived
        :type archived_at: datetime, none_type, optional

        :param closed_at: Timestamp of when the case was closed
        :type closed_at: datetime, none_type, optional

        :param created_at: Timestamp of when the case was created
        :type created_at: datetime, optional

        :param description: Description
        :type description: str, optional

        :param jira_issue: Jira issue attached to case
        :type jira_issue: JiraIssue, none_type, optional

        :param key: Key
        :type key: str, optional

        :param modified_at: Timestamp of when the case was last modified
        :type modified_at: datetime, none_type, optional

        :param priority: Case priority
        :type priority: CasePriority, optional

        :param service_now_ticket: ServiceNow ticket attached to case
        :type service_now_ticket: ServiceNowTicket, none_type, optional

        :param status: Case status
        :type status: CaseStatus, optional

        :param title: Title
        :type title: str, optional

        :param type: Case type
        :type type: CaseType, optional
        """
        if archived_at is not unset:
            kwargs["archived_at"] = archived_at
        if closed_at is not unset:
            kwargs["closed_at"] = closed_at
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if description is not unset:
            kwargs["description"] = description
        if jira_issue is not unset:
            kwargs["jira_issue"] = jira_issue
        if key is not unset:
            kwargs["key"] = key
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if priority is not unset:
            kwargs["priority"] = priority
        if service_now_ticket is not unset:
            kwargs["service_now_ticket"] = service_now_ticket
        if status is not unset:
            kwargs["status"] = status
        if title is not unset:
            kwargs["title"] = title
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
