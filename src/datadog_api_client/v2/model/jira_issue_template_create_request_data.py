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
    from datadog_api_client.v2.model.jira_issue_template_create_request_attributes import (
        JiraIssueTemplateCreateRequestAttributes,
    )
    from datadog_api_client.v2.model.jira_issue_template_type import JiraIssueTemplateType


class JiraIssueTemplateCreateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.jira_issue_template_create_request_attributes import (
            JiraIssueTemplateCreateRequestAttributes,
        )
        from datadog_api_client.v2.model.jira_issue_template_type import JiraIssueTemplateType

        return {
            "attributes": (JiraIssueTemplateCreateRequestAttributes,),
            "type": (JiraIssueTemplateType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[JiraIssueTemplateCreateRequestAttributes, UnsetType] = unset,
        type: Union[JiraIssueTemplateType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for creating a Jira issue template

        :param attributes: Attributes for creating a Jira issue template
        :type attributes: JiraIssueTemplateCreateRequestAttributes, optional

        :param type: Type identifier for Jira issue template resources
        :type type: JiraIssueTemplateType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
