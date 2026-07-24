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
    from datadog_api_client.v2.model.postmortem_template_incident_type_relationship import (
        PostmortemTemplateIncidentTypeRelationship,
    )


class PostmortemTemplateCreateRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.postmortem_template_incident_type_relationship import (
            PostmortemTemplateIncidentTypeRelationship,
        )

        return {
            "incident_type": (PostmortemTemplateIncidentTypeRelationship,),
        }

    attribute_map = {
        "incident_type": "incident_type",
    }

    def __init__(self_, incident_type: Union[PostmortemTemplateIncidentTypeRelationship, UnsetType] = unset, **kwargs):
        """
        Relationships for a postmortem template. ``incident_type`` is required when creating a template and is immutable afterwards.

        :param incident_type: Relationship to the incident type this template belongs to.
        :type incident_type: PostmortemTemplateIncidentTypeRelationship, optional
        """
        if incident_type is not unset:
            kwargs["incident_type"] = incident_type
        super().__init__(kwargs)
