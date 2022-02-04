# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.incident_response_attributes import IncidentResponseAttributes
    from datadog_api_client.v2.model.incident_response_relationships import IncidentResponseRelationships
    from datadog_api_client.v2.model.incident_type import IncidentType

    globals()["IncidentResponseAttributes"] = IncidentResponseAttributes
    globals()["IncidentResponseRelationships"] = IncidentResponseRelationships
    globals()["IncidentType"] = IncidentType


class IncidentResponseData(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "attributes": (IncidentResponseAttributes,),
            "id": (str,),
            "relationships": (IncidentResponseRelationships,),
            "type": (IncidentType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
        "attributes": "attributes",
        "relationships": "relationships",
    }

    read_only_vars = {}

    def __init__(self, id, type, *args, **kwargs):
        """IncidentResponseData - a model defined in OpenAPI


        :param id: The incident's ID.
        :type id: str

        :type type: IncidentType

        :type attributes: IncidentResponseAttributes, optional

        :type relationships: IncidentResponseRelationships, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.id = id
        self.type = type

    @classmethod
    def _from_openapi_data(cls, id, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(IncidentResponseData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.id = id
        self.type = type
        return self
