# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.create_jira_issue_request_data_attributes import (
        CreateJiraIssueRequestDataAttributes,
    )
    from datadog_api_client.v2.model.create_jira_issue_request_data_relationships import (
        CreateJiraIssueRequestDataRelationships,
    )
    from datadog_api_client.v2.model.jira_issues_data_type import JiraIssuesDataType


class CreateJiraIssueRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_jira_issue_request_data_attributes import (
            CreateJiraIssueRequestDataAttributes,
        )
        from datadog_api_client.v2.model.create_jira_issue_request_data_relationships import (
            CreateJiraIssueRequestDataRelationships,
        )
        from datadog_api_client.v2.model.jira_issues_data_type import JiraIssuesDataType

        return {
            "attributes": (CreateJiraIssueRequestDataAttributes,),
            "id": (str,),
            "relationships": (CreateJiraIssueRequestDataRelationships,),
            "type": (JiraIssuesDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        type: JiraIssuesDataType,
        attributes: Union[CreateJiraIssueRequestDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[CreateJiraIssueRequestDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data of the Jira issue to create.

        :param attributes: Attributes of the Jira issue to create.
        :type attributes: CreateJiraIssueRequestDataAttributes, optional

        :param id: The unique identifier of the Jira issue creation request.
        :type id: str, optional

        :param relationships: Relationships of the Jira issue to create.
        :type relationships: CreateJiraIssueRequestDataRelationships, optional

        :param type: Jira issues resource type.
        :type type: JiraIssuesDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
