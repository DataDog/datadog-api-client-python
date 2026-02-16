# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class JiraIssuesMetadataDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "account_id": (str,),
            "issue_type_id": (str,),
            "project_id": (str,),
        }

    attribute_map = {
        "account_id": "account_id",
        "issue_type_id": "issue_type_id",
        "project_id": "project_id",
    }

    def __init__(self_, account_id: str, issue_type_id: str, project_id: str, **kwargs):
        """


        :param account_id: Jira account identifier.
        :type account_id: str

        :param issue_type_id: Jira issue type identifier.
        :type issue_type_id: str

        :param project_id: Jira project identifier.
        :type project_id: str
        """
        super().__init__(kwargs)

        self_.account_id = account_id
        self_.issue_type_id = issue_type_id
        self_.project_id = project_id
