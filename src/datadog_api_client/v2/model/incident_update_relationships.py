# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    date,
    datetime,
    file_type,
    none_type,
)


def lazy_import():
    from datadog_api_client.v2.model.relationship_to_incident_integration_metadatas import (
        RelationshipToIncidentIntegrationMetadatas,
    )
    from datadog_api_client.v2.model.relationship_to_incident_postmortem import RelationshipToIncidentPostmortem
    from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser

    globals()["RelationshipToIncidentIntegrationMetadatas"] = RelationshipToIncidentIntegrationMetadatas
    globals()["RelationshipToIncidentPostmortem"] = RelationshipToIncidentPostmortem
    globals()["RelationshipToUser"] = RelationshipToUser


class IncidentUpdateRelationships(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "commander_user": (RelationshipToUser,),
            "created_by_user": (RelationshipToUser,),
            "integrations": (RelationshipToIncidentIntegrationMetadatas,),
            "last_modified_by_user": (RelationshipToUser,),
            "postmortem": (RelationshipToIncidentPostmortem,),
        }

    attribute_map = {
        "commander_user": "commander_user",
        "created_by_user": "created_by_user",
        "integrations": "integrations",
        "last_modified_by_user": "last_modified_by_user",
        "postmortem": "postmortem",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """IncidentUpdateRelationships - a model defined in OpenAPI

        Keyword Args:
            commander_user (RelationshipToUser): [optional]
            created_by_user (RelationshipToUser): [optional]
            integrations (RelationshipToIncidentIntegrationMetadatas): [optional]
            last_modified_by_user (RelationshipToUser): [optional]
            postmortem (RelationshipToIncidentPostmortem): [optional]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(IncidentUpdateRelationships, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
