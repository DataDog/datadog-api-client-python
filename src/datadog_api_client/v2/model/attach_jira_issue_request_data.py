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
    from datadog_api_client.v2.model.attach_jira_issue_request_data_attributes import (
        AttachJiraIssueRequestDataAttributes,
    )
    from datadog_api_client.v2.model.attach_jira_issue_request_data_relationships import (
        AttachJiraIssueRequestDataRelationships,
    )
    from datadog_api_client.v2.model.jira_issues_data_type import JiraIssuesDataType


class AttachJiraIssueRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.attach_jira_issue_request_data_attributes import (
            AttachJiraIssueRequestDataAttributes,
        )
        from datadog_api_client.v2.model.attach_jira_issue_request_data_relationships import (
            AttachJiraIssueRequestDataRelationships,
        )
        from datadog_api_client.v2.model.jira_issues_data_type import JiraIssuesDataType

        return {
            "attributes": (AttachJiraIssueRequestDataAttributes,),
            "relationships": (AttachJiraIssueRequestDataRelationships,),
            "type": (JiraIssuesDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        type: JiraIssuesDataType,
        attributes: Union[AttachJiraIssueRequestDataAttributes, UnsetType] = unset,
        relationships: Union[AttachJiraIssueRequestDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data of the Jira issue to attach security findings to.

        :param attributes: Attributes of the Jira issue to attach security findings to.
        :type attributes: AttachJiraIssueRequestDataAttributes, optional

        :param relationships: Relationships of the Jira issue to attach security findings to.
        :type relationships: AttachJiraIssueRequestDataRelationships, optional

        :param type: Jira issues resource type.
        :type type: JiraIssuesDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
