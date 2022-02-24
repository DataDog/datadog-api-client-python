# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.incident_service_update_attributes import IncidentServiceUpdateAttributes
    from datadog_api_client.v2.model.incident_service_relationships import IncidentServiceRelationships
    from datadog_api_client.v2.model.incident_service_type import IncidentServiceType

    globals()["IncidentServiceUpdateAttributes"] = IncidentServiceUpdateAttributes
    globals()["IncidentServiceRelationships"] = IncidentServiceRelationships
    globals()["IncidentServiceType"] = IncidentServiceType


class IncidentServiceUpdateData(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "attributes": (IncidentServiceUpdateAttributes,),
            "id": (str,),
            "relationships": (IncidentServiceRelationships,),
            "type": (IncidentServiceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    read_only_vars = {
        "relationships",
    }

    def __init__(self, type, *args, **kwargs):
        """
        Incident Service payload for update requests.

        :param attributes: The incident service's attributes for an update request.
        :type attributes: IncidentServiceUpdateAttributes, optional

        :param id: The incident service's ID.
        :type id: str, optional

        :param relationships: The incident service's relationships.
        :type relationships: IncidentServiceRelationships, optional

        :param type: Incident service resource type.
        :type type: IncidentServiceType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.type = type

    @classmethod
    def _from_openapi_data(cls, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(IncidentServiceUpdateData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.type = type
        return self
