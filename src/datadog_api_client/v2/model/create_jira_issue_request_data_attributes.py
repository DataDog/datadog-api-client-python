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
    from datadog_api_client.v2.model.create_jira_issue_request_data_attributes_fields import (
        CreateJiraIssueRequestDataAttributesFields,
    )


class CreateJiraIssueRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_jira_issue_request_data_attributes_fields import (
            CreateJiraIssueRequestDataAttributesFields,
        )

        return {
            "fields": (CreateJiraIssueRequestDataAttributesFields,),
        }

    attribute_map = {
        "fields": "fields",
    }

    def __init__(self_, fields: Union[CreateJiraIssueRequestDataAttributesFields, UnsetType] = unset, **kwargs):
        """
        Attributes of the Jira issue to create.

        :param fields: Custom fields of the Jira issue to create. For the list of available fields, see `Jira documentation <https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issues/#api-rest-api-2-issue-createmeta-projectidorkey-issuetypes-issuetypeid-get>`_.
        :type fields: CreateJiraIssueRequestDataAttributesFields, optional
        """
        if fields is not unset:
            kwargs["fields"] = fields
        super().__init__(kwargs)
