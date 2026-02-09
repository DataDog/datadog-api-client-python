# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

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


class JiraIssueCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
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
            "jira_account_id": (str,),
            "project_id": (str,),
        }

    attribute_map = {
        "fields": "fields",
        "issue_type_id": "issue_type_id",
        "jira_account_id": "jira_account_id",
        "project_id": "project_id",
    }

    def __init__(
        self_,
        issue_type_id: str,
        jira_account_id: str,
        project_id: str,
        fields: Union[Dict[str, Any], UnsetType] = unset,
        **kwargs,
    ):
        """
        Jira issue creation attributes

        :param fields: Additional Jira fields
        :type fields: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param issue_type_id: Jira issue type ID
        :type issue_type_id: str

        :param jira_account_id: Jira account ID
        :type jira_account_id: str

        :param project_id: Jira project ID
        :type project_id: str
        """
        if fields is not unset:
            kwargs["fields"] = fields
        super().__init__(kwargs)

        self_.issue_type_id = issue_type_id
        self_.jira_account_id = jira_account_id
        self_.project_id = project_id
