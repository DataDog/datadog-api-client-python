# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_response_attributes import IncidentResponseAttributes
        from datadog_api_client.v2.model.incident_response_relationships import IncidentResponseRelationships
        from datadog_api_client.v2.model.incident_type import IncidentType

        return {
            "attributes": (IncidentResponseAttributes,),
            "id": (str,),
            "relationships": (IncidentResponseRelationships,),
            "type": (IncidentType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(self, id, type, *args, **kwargs):
        """
        Incident data from a response.

        :param attributes: The incident's attributes from a response.
        :type attributes: IncidentResponseAttributes, optional

        :param id: The incident's ID.
        :type id: str

        :param relationships: The incident's relationships from a response.
        :type relationships: IncidentResponseRelationships, optional

        :param type: Incident resource type.
        :type type: IncidentType
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
