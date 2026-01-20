# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    UUID,
)


class JiraIssueTemplateDataAttributes(ModelNormal):
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
            "name": (str,),
            "project_id": (str,),
        }

    attribute_map = {
        "fields": "fields",
        "issue_type_id": "issue_type_id",
        "name": "name",
        "project_id": "project_id",
    }

    def __init__(self_, fields: Dict[str, Any], issue_type_id: str, name: str, project_id: str, **kwargs):
        """
        Attributes of a Jira issue template

        :param fields: Custom fields for the Jira issue template
        :type fields: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}

        :param issue_type_id: The ID of the Jira issue type
        :type issue_type_id: str

        :param name: The name of the issue template
        :type name: str

        :param project_id: The ID of the Jira project
        :type project_id: str
        """
        super().__init__(kwargs)

        self_.fields = fields
        self_.issue_type_id = issue_type_id
        self_.name = name
        self_.project_id = project_id
