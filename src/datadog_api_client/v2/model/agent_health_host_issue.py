# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AgentHealthHostIssue(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "category": (str,),
            "issue_id": (str,),
            "issue_name": (str,),
            "issue_type": (str,),
        }

    attribute_map = {
        "category": "category",
        "issue_id": "issue_id",
        "issue_name": "issue_name",
        "issue_type": "issue_type",
    }

    def __init__(self_, category: str, issue_id: str, issue_name: str, issue_type: str, **kwargs):
        """
        An active Agent Health issue associated with a resource.

        :param category: The category used by the Agent to group and reconcile the issue.
        :type category: str

        :param issue_id: The unique identifier of the issue.
        :type issue_id: str

        :param issue_name: The human-readable name of the issue.
        :type issue_name: str

        :param issue_type: The machine-readable type of the issue.
        :type issue_type: str
        """
        super().__init__(kwargs)

        self_.category = category
        self_.issue_id = issue_id
        self_.issue_name = issue_name
        self_.issue_type = issue_type
