# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser
    from datadog_api_client.v2.model.case_insights_items import CaseInsightsItems
    from datadog_api_client.v2.model.finding_jira_issue import FindingJiraIssue


class FindingCaseResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser
        from datadog_api_client.v2.model.case_insights_items import CaseInsightsItems
        from datadog_api_client.v2.model.finding_jira_issue import FindingJiraIssue

        return {
            "archived_at": (datetime,),
            "assigned_to": (RelationshipToUser,),
            "attributes": ({str: ([str],)},),
            "closed_at": (datetime,),
            "created_at": (datetime,),
            "creation_source": (str,),
            "description": (str,),
            "due_date": (str,),
            "insights": ([CaseInsightsItems],),
            "jira_issue": (FindingJiraIssue,),
            "key": (str,),
            "modified_at": (datetime,),
            "priority": (str,),
            "status": (str,),
            "status_group": (str,),
            "status_name": (str,),
            "title": (str,),
            "type": (str,),
        }

    attribute_map = {
        "archived_at": "archived_at",
        "assigned_to": "assigned_to",
        "attributes": "attributes",
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
        "status_group": "status_group",
        "status_name": "status_name",
        "title": "title",
        "type": "type",
    }

    def __init__(
        self_,
        archived_at: Union[datetime, UnsetType] = unset,
        assigned_to: Union[RelationshipToUser, UnsetType] = unset,
        attributes: Union[Dict[str, List[str]], UnsetType] = unset,
        closed_at: Union[datetime, UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        creation_source: Union[str, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        due_date: Union[str, UnsetType] = unset,
        insights: Union[List[CaseInsightsItems], UnsetType] = unset,
        jira_issue: Union[FindingJiraIssue, UnsetType] = unset,
        key: Union[str, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        priority: Union[str, UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        status_group: Union[str, UnsetType] = unset,
        status_name: Union[str, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the case.

        :param archived_at: Timestamp of when the case was archived.
        :type archived_at: datetime, optional

        :param assigned_to: Relationship to user.
        :type assigned_to: RelationshipToUser, optional

        :param attributes:
        :type attributes: {str: ([str],)}, optional

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
        :type insights: [CaseInsightsItems], optional

        :param jira_issue: Jira issue associated with the case.
        :type jira_issue: FindingJiraIssue, optional

        :param key: Key of the case.
        :type key: str, optional

        :param modified_at: Timestamp of when the case was last modified.
        :type modified_at: datetime, optional

        :param priority: Priority of the case.
        :type priority: str, optional

        :param status: Status of the case.
        :type status: str, optional

        :param status_group: Status group of the case.
        :type status_group: str, optional

        :param status_name: Status name of the case.
        :type status_name: str, optional

        :param title: Title of the case.
        :type title: str, optional

        :param type: Type of the case. For security cases, this is always "SECURITY".
        :type type: str, optional
        """
        if archived_at is not unset:
            kwargs["archived_at"] = archived_at
        if assigned_to is not unset:
            kwargs["assigned_to"] = assigned_to
        if attributes is not unset:
            kwargs["attributes"] = attributes
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
        if status_group is not unset:
            kwargs["status_group"] = status_group
        if status_name is not unset:
            kwargs["status_name"] = status_name
        if title is not unset:
            kwargs["title"] = title
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
