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
    from datadog_api_client.v2.model.incident_jira_template_incident_type_relationship import (
        IncidentJiraTemplateIncidentTypeRelationship,
    )


class IncidentJiraTemplateRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_jira_template_incident_type_relationship import (
            IncidentJiraTemplateIncidentTypeRelationship,
        )

        return {
            "incident_type": (IncidentJiraTemplateIncidentTypeRelationship,),
        }

    attribute_map = {
        "incident_type": "incident_type",
    }

    def __init__(
        self_, incident_type: Union[IncidentJiraTemplateIncidentTypeRelationship, UnsetType] = unset, **kwargs
    ):
        """
        Relationships for an incident Jira template.

        :param incident_type: Relationship to an incident type.
        :type incident_type: IncidentJiraTemplateIncidentTypeRelationship, optional
        """
        if incident_type is not unset:
            kwargs["incident_type"] = incident_type
        super().__init__(kwargs)
