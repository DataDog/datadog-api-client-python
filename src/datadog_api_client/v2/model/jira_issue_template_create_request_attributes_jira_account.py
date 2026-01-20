# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


class JiraIssueTemplateCreateRequestAttributesJiraAccount(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (UUID,),
        }

    attribute_map = {
        "id": "id",
    }

    def __init__(self_, id: UUID, **kwargs):
        """
        Reference to the Jira account

        :param id: The ID of the Jira account
        :type id: UUID
        """
        super().__init__(kwargs)

        self_.id = id
