# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.jira_issue_custom_fields import JiraIssueCustomFields
    from datadog_api_client.v2.model.jira_issue_data_attributes_request_mode import JiraIssueDataAttributesRequestMode


class JiraIssueDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.jira_issue_custom_fields import JiraIssueCustomFields
        from datadog_api_client.v2.model.jira_issue_data_attributes_request_mode import (
            JiraIssueDataAttributesRequestMode,
        )

        return {
            "account_id": (str,),
            "fields": (JiraIssueCustomFields,),
            "issue_type": (str,),
            "issuetype_id": (str,),
            "mode": (JiraIssueDataAttributesRequestMode,),
            "project_id": (str,),
            "project_key": (str,),
        }

    attribute_map = {
        "account_id": "account_id",
        "fields": "fields",
        "issue_type": "issue_type",
        "issuetype_id": "issuetype_id",
        "mode": "mode",
        "project_id": "project_id",
        "project_key": "project_key",
    }

    def __init__(
        self_,
        account_id: str,
        issue_type: str,
        issuetype_id: str,
        project_id: str,
        project_key: str,
        fields: Union[JiraIssueCustomFields, none_type, UnsetType] = unset,
        mode: Union[JiraIssueDataAttributesRequestMode, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param account_id: Jira account identifier.
        :type account_id: str

        :param fields: Custom fields for the Jira issue.
        :type fields: JiraIssueCustomFields, none_type, optional

        :param issue_type: Jira issue type name.
        :type issue_type: str

        :param issuetype_id: Jira issue type identifier.
        :type issuetype_id: str

        :param mode: Mode for creating the Jira issue. Can be "single" or "multiple".
        :type mode: JiraIssueDataAttributesRequestMode, optional

        :param project_id: Jira project identifier.
        :type project_id: str

        :param project_key: Jira project key.
        :type project_key: str
        """
        if fields is not unset:
            kwargs["fields"] = fields
        if mode is not unset:
            kwargs["mode"] = mode
        super().__init__(kwargs)

        self_.account_id = account_id
        self_.issue_type = issue_type
        self_.issuetype_id = issuetype_id
        self_.project_id = project_id
        self_.project_key = project_key
