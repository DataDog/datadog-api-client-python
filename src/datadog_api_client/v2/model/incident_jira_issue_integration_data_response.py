# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_jira_issue_integration_data_attributes import (
        IncidentJiraIssueIntegrationDataAttributes,
    )
    from datadog_api_client.v2.model.incident_jira_issue_integration_type import IncidentJiraIssueIntegrationType


class IncidentJiraIssueIntegrationDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_jira_issue_integration_data_attributes import (
            IncidentJiraIssueIntegrationDataAttributes,
        )
        from datadog_api_client.v2.model.incident_jira_issue_integration_type import IncidentJiraIssueIntegrationType

        return {
            "attributes": (IncidentJiraIssueIntegrationDataAttributes,),
            "id": (UUID,),
            "type": (IncidentJiraIssueIntegrationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentJiraIssueIntegrationDataAttributes,
        id: UUID,
        type: IncidentJiraIssueIntegrationType,
        **kwargs,
    ):
        """
        Jira issue integration data in a response.

        :param attributes: Attributes of a Jira issue integration.
        :type attributes: IncidentJiraIssueIntegrationDataAttributes

        :param id: The integration identifier.
        :type id: UUID

        :param type: Incident integration resource type.
        :type type: IncidentJiraIssueIntegrationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
