# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_create_attributes import IncidentCreateAttributes
        from datadog_api_client.v2.model.incident_create_relationships import IncidentCreateRelationships
        from datadog_api_client.v2.model.incident_type import IncidentType

        return {
            "attributes": (IncidentCreateAttributes,),
            "relationships": (IncidentCreateRelationships,),
            "type": (IncidentType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(self, attributes, type, *args, **kwargs):
        """
        Incident data for a create request.

        :param attributes: The incident's attributes for a create request.
        :type attributes: IncidentCreateAttributes

        :param relationships: The relationships the incident will have with other resources once created.
        :type relationships: IncidentCreateRelationships, optional

        :param type: Incident resource type.
        :type type: IncidentType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.type = type

    @classmethod
    def _from_openapi_data(cls, attributes, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(IncidentCreateData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.type = type
        return self
