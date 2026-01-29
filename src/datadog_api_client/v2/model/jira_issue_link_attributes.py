# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class JiraIssueLinkAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "jira_issue_url": (str,),
        }

    attribute_map = {
        "jira_issue_url": "jira_issue_url",
    }

    def __init__(self_, jira_issue_url: str, **kwargs):
        """
        Jira issue link attributes

        :param jira_issue_url: URL of the Jira issue
        :type jira_issue_url: str
        """
        super().__init__(kwargs)

        self_.jira_issue_url = jira_issue_url
