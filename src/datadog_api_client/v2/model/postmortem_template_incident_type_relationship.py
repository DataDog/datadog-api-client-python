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
    from datadog_api_client.v2.model.postmortem_template_incident_type_relationship_data import (
        PostmortemTemplateIncidentTypeRelationshipData,
    )


class PostmortemTemplateIncidentTypeRelationship(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.postmortem_template_incident_type_relationship_data import (
            PostmortemTemplateIncidentTypeRelationshipData,
        )

        return {
            "data": (PostmortemTemplateIncidentTypeRelationshipData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: PostmortemTemplateIncidentTypeRelationshipData, **kwargs):
        """
        Relationship to the incident type this template belongs to.

        :param data: Incident type relationship data.
        :type data: PostmortemTemplateIncidentTypeRelationshipData
        """
        super().__init__(kwargs)

        self_.data = data
