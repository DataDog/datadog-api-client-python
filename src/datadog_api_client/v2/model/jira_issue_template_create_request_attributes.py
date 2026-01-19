# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.jira_issue_template_create_request_attributes_jira_account import (
        JiraIssueTemplateCreateRequestAttributesJiraAccount,
    )


class JiraIssueTemplateCreateRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.jira_issue_template_create_request_attributes_jira_account import (
            JiraIssueTemplateCreateRequestAttributesJiraAccount,
        )

        return {
            "fields": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "issue_type_id": (str,),
            "jira_account": (JiraIssueTemplateCreateRequestAttributesJiraAccount,),
            "name": (str,),
            "project_id": (str,),
        }

    attribute_map = {
        "fields": "fields",
        "issue_type_id": "issue_type_id",
        "jira_account": "jira-account",
        "name": "name",
        "project_id": "project_id",
    }

    def __init__(
        self_,
        fields: Union[Dict[str, Any], UnsetType] = unset,
        issue_type_id: Union[str, UnsetType] = unset,
        jira_account: Union[JiraIssueTemplateCreateRequestAttributesJiraAccount, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        project_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating a Jira issue template

        :param fields: Custom fields for the Jira issue template
        :type fields: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param issue_type_id: The ID of the Jira issue type
        :type issue_type_id: str, optional

        :param jira_account: Reference to the Jira account
        :type jira_account: JiraIssueTemplateCreateRequestAttributesJiraAccount, optional

        :param name: The name of the issue template
        :type name: str, optional

        :param project_id: The ID of the Jira project
        :type project_id: str, optional
        """
        if fields is not unset:
            kwargs["fields"] = fields
        if issue_type_id is not unset:
            kwargs["issue_type_id"] = issue_type_id
        if jira_account is not unset:
            kwargs["jira_account"] = jira_account
        if name is not unset:
            kwargs["name"] = name
        if project_id is not unset:
            kwargs["project_id"] = project_id
        super().__init__(kwargs)
