# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser
    from datadog_api_client.v2.model.incident_type_relationships_google_meet_configuration import (
        IncidentTypeRelationshipsGoogleMeetConfiguration,
    )
    from datadog_api_client.v2.model.incident_type_relationships_microsoft_teams_configuration import (
        IncidentTypeRelationshipsMicrosoftTeamsConfiguration,
    )
    from datadog_api_client.v2.model.incident_type_relationships_zoom_configuration import (
        IncidentTypeRelationshipsZoomConfiguration,
    )


class IncidentTypeRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser
        from datadog_api_client.v2.model.incident_type_relationships_google_meet_configuration import (
            IncidentTypeRelationshipsGoogleMeetConfiguration,
        )
        from datadog_api_client.v2.model.incident_type_relationships_microsoft_teams_configuration import (
            IncidentTypeRelationshipsMicrosoftTeamsConfiguration,
        )
        from datadog_api_client.v2.model.incident_type_relationships_zoom_configuration import (
            IncidentTypeRelationshipsZoomConfiguration,
        )

        return {
            "created_by_user": (RelationshipToUser,),
            "google_meet_configuration": (IncidentTypeRelationshipsGoogleMeetConfiguration,),
            "last_modified_by_user": (RelationshipToUser,),
            "microsoft_teams_configuration": (IncidentTypeRelationshipsMicrosoftTeamsConfiguration,),
            "zoom_configuration": (IncidentTypeRelationshipsZoomConfiguration,),
        }

    attribute_map = {
        "created_by_user": "created_by_user",
        "google_meet_configuration": "google_meet_configuration",
        "last_modified_by_user": "last_modified_by_user",
        "microsoft_teams_configuration": "microsoft_teams_configuration",
        "zoom_configuration": "zoom_configuration",
    }

    def __init__(
        self_,
        created_by_user: Union[RelationshipToUser, UnsetType] = unset,
        google_meet_configuration: Union[
            IncidentTypeRelationshipsGoogleMeetConfiguration, none_type, UnsetType
        ] = unset,
        last_modified_by_user: Union[RelationshipToUser, UnsetType] = unset,
        microsoft_teams_configuration: Union[
            IncidentTypeRelationshipsMicrosoftTeamsConfiguration, none_type, UnsetType
        ] = unset,
        zoom_configuration: Union[IncidentTypeRelationshipsZoomConfiguration, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        The incident type's resource relationships.

        :param created_by_user: Relationship to user.
        :type created_by_user: RelationshipToUser, optional

        :param google_meet_configuration: The definition of ``IncidentTypeRelationshipsGoogleMeetConfiguration`` object.
        :type google_meet_configuration: IncidentTypeRelationshipsGoogleMeetConfiguration, none_type, optional

        :param last_modified_by_user: Relationship to user.
        :type last_modified_by_user: RelationshipToUser, optional

        :param microsoft_teams_configuration: The definition of ``IncidentTypeRelationshipsMicrosoftTeamsConfiguration`` object.
        :type microsoft_teams_configuration: IncidentTypeRelationshipsMicrosoftTeamsConfiguration, none_type, optional

        :param zoom_configuration: The definition of ``IncidentTypeRelationshipsZoomConfiguration`` object.
        :type zoom_configuration: IncidentTypeRelationshipsZoomConfiguration, none_type, optional
        """
        if created_by_user is not unset:
            kwargs["created_by_user"] = created_by_user
        if google_meet_configuration is not unset:
            kwargs["google_meet_configuration"] = google_meet_configuration
        if last_modified_by_user is not unset:
            kwargs["last_modified_by_user"] = last_modified_by_user
        if microsoft_teams_configuration is not unset:
            kwargs["microsoft_teams_configuration"] = microsoft_teams_configuration
        if zoom_configuration is not unset:
            kwargs["zoom_configuration"] = zoom_configuration
        super().__init__(kwargs)
