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
    UUID,
)


class IncidentJiraIssueDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "account_id": (str,),
            "issue_type_id": (str,),
            "project_id": (str,),
            "template_id": (UUID,),
        }

    attribute_map = {
        "account_id": "account_id",
        "issue_type_id": "issue_type_id",
        "project_id": "project_id",
        "template_id": "template_id",
    }

    def __init__(
        self_,
        account_id: str,
        issue_type_id: str,
        project_id: str,
        template_id: Union[UUID, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating a Jira issue from an incident.

        :param account_id: The Jira account identifier.
        :type account_id: str

        :param issue_type_id: The Jira issue type identifier.
        :type issue_type_id: str

        :param project_id: The Jira project identifier.
        :type project_id: str

        :param template_id: The identifier of the Jira template to use.
        :type template_id: UUID, optional
        """
        if template_id is not unset:
            kwargs["template_id"] = template_id
        super().__init__(kwargs)

        self_.account_id = account_id
        self_.issue_type_id = issue_type_id
        self_.project_id = project_id
