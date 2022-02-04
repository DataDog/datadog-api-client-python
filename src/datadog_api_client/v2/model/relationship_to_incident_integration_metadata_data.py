# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.incident_integration_metadata_type import IncidentIntegrationMetadataType

    globals()["IncidentIntegrationMetadataType"] = IncidentIntegrationMetadataType


class RelationshipToIncidentIntegrationMetadataData(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "id": (str,),
            "type": (IncidentIntegrationMetadataType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    read_only_vars = {}

    def __init__(self, id, type, *args, **kwargs):
        """RelationshipToIncidentIntegrationMetadataData - a model defined in OpenAPI


        :param id: A unique identifier that represents the integration metadata.
        :type id: str

        :type type: IncidentIntegrationMetadataType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.id = id
        self.type = type

    @classmethod
    def _from_openapi_data(cls, id, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(RelationshipToIncidentIntegrationMetadataData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.id = id
        self.type = type
        return self
