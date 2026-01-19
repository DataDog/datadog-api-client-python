# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.jira_account_relationship import JiraAccountRelationship


class JiraIssueTemplateDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.jira_account_relationship import JiraAccountRelationship

        return {
            "jira_account": (JiraAccountRelationship,),
        }

    attribute_map = {
        "jira_account": "jira-account",
    }

    def __init__(self_, jira_account: JiraAccountRelationship, **kwargs):
        """
        Relationships of a Jira issue template

        :param jira_account: Relationship to a Jira account
        :type jira_account: JiraAccountRelationship
        """
        super().__init__(kwargs)

        self_.jira_account = jira_account
