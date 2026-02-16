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
    from datadog_api_client.v2.model.jira_issue_data_attributes_request import JiraIssueDataAttributesRequest
    from datadog_api_client.v2.model.jira_issue_data_meta import JiraIssueDataMeta
    from datadog_api_client.v2.model.jira_issue_type import JiraIssueType


class JiraIssueDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.jira_issue_data_attributes_request import JiraIssueDataAttributesRequest
        from datadog_api_client.v2.model.jira_issue_data_meta import JiraIssueDataMeta
        from datadog_api_client.v2.model.jira_issue_type import JiraIssueType

        return {
            "attributes": (JiraIssueDataAttributesRequest,),
            "id": (str,),
            "meta": (JiraIssueDataMeta,),
            "type": (JiraIssueType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "meta": "meta",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: JiraIssueDataAttributesRequest,
        id: str,
        meta: JiraIssueDataMeta,
        type: JiraIssueType,
        **kwargs,
    ):
        """


        :param attributes:
        :type attributes: JiraIssueDataAttributesRequest

        :param id: Unique identifier of the Jira issue request.
        :type id: str

        :param meta:
        :type meta: JiraIssueDataMeta

        :param type: Jira issue resource type.
        :type type: JiraIssueType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.meta = meta
        self_.type = type
