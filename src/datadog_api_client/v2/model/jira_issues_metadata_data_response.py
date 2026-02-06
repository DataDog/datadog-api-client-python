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
    from datadog_api_client.v2.model.jira_issues_metadata_data_attributes_response import (
        JiraIssuesMetadataDataAttributesResponse,
    )
    from datadog_api_client.v2.model.jira_issues_metadata_type import JiraIssuesMetadataType


class JiraIssuesMetadataDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.jira_issues_metadata_data_attributes_response import (
            JiraIssuesMetadataDataAttributesResponse,
        )
        from datadog_api_client.v2.model.jira_issues_metadata_type import JiraIssuesMetadataType

        return {
            "attributes": (JiraIssuesMetadataDataAttributesResponse,),
            "id": (str,),
            "type": (JiraIssuesMetadataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: JiraIssuesMetadataDataAttributesResponse, id: str, type: JiraIssuesMetadataType, **kwargs
    ):
        """


        :param attributes:
        :type attributes: JiraIssuesMetadataDataAttributesResponse

        :param id: Jira issue URL.
        :type id: str

        :param type: Jira issues metadata resource type.
        :type type: JiraIssuesMetadataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
