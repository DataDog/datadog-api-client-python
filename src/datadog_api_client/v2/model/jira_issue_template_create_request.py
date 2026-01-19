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
    from datadog_api_client.v2.model.jira_issue_template_create_request_data import JiraIssueTemplateCreateRequestData


class JiraIssueTemplateCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.jira_issue_template_create_request_data import (
            JiraIssueTemplateCreateRequestData,
        )

        return {
            "data": (JiraIssueTemplateCreateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[JiraIssueTemplateCreateRequestData, UnsetType] = unset, **kwargs):
        """
        Request to create a Jira issue template

        :param data: Data object for creating a Jira issue template
        :type data: JiraIssueTemplateCreateRequestData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
