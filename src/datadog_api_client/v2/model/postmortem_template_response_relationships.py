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
    from datadog_api_client.v2.model.postmortem_template_user_relationship import PostmortemTemplateUserRelationship


class PostmortemTemplateResponseRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.postmortem_template_incident_type_relationship import (
            PostmortemTemplateIncidentTypeRelationship,
        )
        from datadog_api_client.v2.model.postmortem_template_user_relationship import PostmortemTemplateUserRelationship

        return {
            "incident_type": (PostmortemTemplateIncidentTypeRelationship,),
            "last_modified_by_user": (PostmortemTemplateUserRelationship,),
        }

    attribute_map = {
        "incident_type": "incident_type",
        "last_modified_by_user": "last_modified_by_user",
    }

    def __init__(
        self_,
        incident_type: Union[PostmortemTemplateIncidentTypeRelationship, UnsetType] = unset,
        last_modified_by_user: Union[PostmortemTemplateUserRelationship, UnsetType] = unset,
        **kwargs,
    ):
        """
        Relationships of a postmortem template returned in a response.

        :param incident_type: Relationship to the incident type this template belongs to.
        :type incident_type: PostmortemTemplateIncidentTypeRelationship, optional

        :param last_modified_by_user: Relationship to a user.
        :type last_modified_by_user: PostmortemTemplateUserRelationship, optional
        """
        if incident_type is not unset:
            kwargs["incident_type"] = incident_type
        if last_modified_by_user is not unset:
            kwargs["last_modified_by_user"] = last_modified_by_user
        super().__init__(kwargs)
