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
    from datadog_api_client.v2.model.create_jira_issue_request_data_relationships_case import (
        CreateJiraIssueRequestDataRelationshipsCase,
    )


class CreateJiraIssueRequestDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_jira_issue_request_data_relationships_case import (
            CreateJiraIssueRequestDataRelationshipsCase,
        )

        return {
            "case": (CreateJiraIssueRequestDataRelationshipsCase,),
        }

    attribute_map = {
        "case": "case",
    }

    def __init__(self_, case: CreateJiraIssueRequestDataRelationshipsCase, **kwargs):
        """
        Relationships of the Jira issue to create.

        :param case: Case linked to the Jira issue.
        :type case: CreateJiraIssueRequestDataRelationshipsCase
        """
        super().__init__(kwargs)

        self_.case = case
