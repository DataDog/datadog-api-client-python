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
    from datadog_api_client.v2.model.incident_service_relationships import IncidentServiceRelationships
    from datadog_api_client.v2.model.incident_service_response_attributes import IncidentServiceResponseAttributes
    from datadog_api_client.v2.model.incident_service_type import IncidentServiceType

    globals()["IncidentServiceRelationships"] = IncidentServiceRelationships
    globals()["IncidentServiceResponseAttributes"] = IncidentServiceResponseAttributes
    globals()["IncidentServiceType"] = IncidentServiceType


class IncidentServiceResponseData(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "attributes": (IncidentServiceResponseAttributes,),
            "id": (str,),
            "relationships": (IncidentServiceRelationships,),
            "type": (IncidentServiceType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
        "attributes": "attributes",
        "relationships": "relationships",
    }

    read_only_vars = {}

    def __init__(self, id, type, *args, **kwargs):
        """IncidentServiceResponseData - a model defined in OpenAPI

        Args:
            id (str): The incident service's ID.
            type (IncidentServiceType):

        Keyword Args:
            attributes (IncidentServiceResponseAttributes): [optional]
            relationships (IncidentServiceRelationships): [optional]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.id = id
        self.type = type

    @classmethod
    def _from_openapi_data(cls, id, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(IncidentServiceResponseData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.id = id
        self.type = type
        return self
