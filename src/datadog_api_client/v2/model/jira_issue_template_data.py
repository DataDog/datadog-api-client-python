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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.jira_issue_template_data_attributes import JiraIssueTemplateDataAttributes
    from datadog_api_client.v2.model.jira_issue_template_data_relationships import JiraIssueTemplateDataRelationships
    from datadog_api_client.v2.model.jira_issue_template_type import JiraIssueTemplateType


class JiraIssueTemplateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.jira_issue_template_data_attributes import JiraIssueTemplateDataAttributes
        from datadog_api_client.v2.model.jira_issue_template_data_relationships import (
            JiraIssueTemplateDataRelationships,
        )
        from datadog_api_client.v2.model.jira_issue_template_type import JiraIssueTemplateType

        return {
            "attributes": (JiraIssueTemplateDataAttributes,),
            "id": (UUID,),
            "relationships": (JiraIssueTemplateDataRelationships,),
            "type": (JiraIssueTemplateType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: JiraIssueTemplateDataAttributes,
        id: UUID,
        type: JiraIssueTemplateType,
        relationships: Union[JiraIssueTemplateDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for a Jira issue template

        :param attributes: Attributes of a Jira issue template
        :type attributes: JiraIssueTemplateDataAttributes

        :param id: Unique identifier for the Jira issue template
        :type id: UUID

        :param relationships: Relationships of a Jira issue template
        :type relationships: JiraIssueTemplateDataRelationships, optional

        :param type: Type identifier for Jira issue template resources
        :type type: JiraIssueTemplateType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
