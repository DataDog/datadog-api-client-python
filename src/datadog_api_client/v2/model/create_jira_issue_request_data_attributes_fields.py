# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class CreateJiraIssueRequestDataAttributesFields(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "fields": (dict,),
        }

    attribute_map = {
        "fields": "fields",
    }

    def __init__(self_, fields: Union[dict, UnsetType] = unset, **kwargs):
        """
        Custom fields of the Jira issue to create. For the list of available fields, see `Jira documentation <https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issues/#api-rest-api-2-issue-createmeta-projectidorkey-issuetypes-issuetypeid-get>`_.

        :param fields:
        :type fields: dict, optional
        """
        if fields is not unset:
            kwargs["fields"] = fields
        super().__init__(kwargs)
