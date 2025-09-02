# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.issue_case_insight import IssueCaseInsight
    from datadog_api_client.v2.model.issue_case_jira_issue import IssueCaseJiraIssue
    from datadog_api_client.v2.model.case_priority import CasePriority
    from datadog_api_client.v2.model.case_status import CaseStatus


class IssueCaseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_case_insight import IssueCaseInsight
        from datadog_api_client.v2.model.issue_case_jira_issue import IssueCaseJiraIssue
        from datadog_api_client.v2.model.case_priority import CasePriority
        from datadog_api_client.v2.model.case_status import CaseStatus

        return {
            "archived_at": (datetime,),
            "closed_at": (datetime,),
            "created_at": (datetime,),
            "creation_source": (str,),
            "description": (str,),
            "due_date": (str,),
            "insights": ([IssueCaseInsight],),
            "jira_issue": (IssueCaseJiraIssue,),
            "key": (str,),
            "modified_at": (datetime,),
            "priority": (CasePriority,),
            "status": (CaseStatus,),
            "title": (str,),
            "type": (str,),
        }

    attribute_map = {
        "archived_at": "archived_at",
        "closed_at": "closed_at",
        "created_at": "created_at",
        "creation_source": "creation_source",
        "description": "description",
        "due_date": "due_date",
        "insights": "insights",
        "jira_issue": "jira_issue",
        "key": "key",
        "modified_at": "modified_at",
        "priority": "priority",
        "status": "status",
        "title": "title",
        "type": "type",
    }

    def __init__(
        self_,
        archived_at: Union[datetime, UnsetType] = unset,
        closed_at: Union[datetime, UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        creation_source: Union[str, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        due_date: Union[str, UnsetType] = unset,
        insights: Union[List[IssueCaseInsight], UnsetType] = unset,
        jira_issue: Union[IssueCaseJiraIssue, UnsetType] = unset,
        key: Union[str, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        priority: Union[CasePriority, UnsetType] = unset,
        status: Union[CaseStatus, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object containing the information of a case.

        :param archived_at: Timestamp of when the case was archived.
        :type archived_at: datetime, optional

        :param closed_at: Timestamp of when the case was closed.
        :type closed_at: datetime, optional

        :param created_at: Timestamp of when the case was created.
        :type created_at: datetime, optional

        :param creation_source: Source of the case creation.
        :type creation_source: str, optional

        :param description: Description of the case.
        :type description: str, optional

        :param due_date: Due date of the case.
        :type due_date: str, optional

        :param insights: Insights of the case.
        :type insights: [IssueCaseInsight], optional

        :param jira_issue: Jira issue of the case.
        :type jira_issue: IssueCaseJiraIssue, optional

        :param key: Key of the case.
        :type key: str, optional

        :param modified_at: Timestamp of when the case was last modified.
        :type modified_at: datetime, optional

        :param priority: Case priority
        :type priority: CasePriority, optional

        :param status: Case status
        :type status: CaseStatus, optional

        :param title: Title of the case.
        :type title: str, optional

        :param type: Type of the case.
        :type type: str, optional
        """
        if archived_at is not unset:
            kwargs["archived_at"] = archived_at
        if closed_at is not unset:
            kwargs["closed_at"] = closed_at
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if creation_source is not unset:
            kwargs["creation_source"] = creation_source
        if description is not unset:
            kwargs["description"] = description
        if due_date is not unset:
            kwargs["due_date"] = due_date
        if insights is not unset:
            kwargs["insights"] = insights
        if jira_issue is not unset:
            kwargs["jira_issue"] = jira_issue
        if key is not unset:
            kwargs["key"] = key
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if priority is not unset:
            kwargs["priority"] = priority
        if status is not unset:
            kwargs["status"] = status
        if title is not unset:
            kwargs["title"] = title
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
