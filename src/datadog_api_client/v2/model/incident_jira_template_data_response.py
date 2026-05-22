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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_jira_template_data_attributes_response import (
        IncidentJiraTemplateDataAttributesResponse,
    )
    from datadog_api_client.v2.model.incident_jira_template_relationships import IncidentJiraTemplateRelationships
    from datadog_api_client.v2.model.incident_jira_template_type import IncidentJiraTemplateType


class IncidentJiraTemplateDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_jira_template_data_attributes_response import (
            IncidentJiraTemplateDataAttributesResponse,
        )
        from datadog_api_client.v2.model.incident_jira_template_relationships import IncidentJiraTemplateRelationships
        from datadog_api_client.v2.model.incident_jira_template_type import IncidentJiraTemplateType

        return {
            "attributes": (IncidentJiraTemplateDataAttributesResponse,),
            "id": (UUID,),
            "relationships": (IncidentJiraTemplateRelationships,),
            "type": (IncidentJiraTemplateType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IncidentJiraTemplateDataAttributesResponse,
        id: UUID,
        type: IncidentJiraTemplateType,
        relationships: Union[IncidentJiraTemplateRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Incident Jira template data in a response.

        :param attributes: Attributes of an incident Jira template.
        :type attributes: IncidentJiraTemplateDataAttributesResponse

        :param id: The template identifier.
        :type id: UUID

        :param relationships: Relationships for an incident Jira template.
        :type relationships: IncidentJiraTemplateRelationships, optional

        :param type: Incident Jira template resource type.
        :type type: IncidentJiraTemplateType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
