# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class OpsgenieServiceResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.opsgenie_service_response_attributes import OpsgenieServiceResponseAttributes
        from datadog_api_client.v2.model.opsgenie_service_type import OpsgenieServiceType

        return {
            "attributes": (OpsgenieServiceResponseAttributes,),
            "id": (str,),
            "type": (OpsgenieServiceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self, attributes, id, type, *args, **kwargs):
        """
        Opsgenie service data from a response.

        :param attributes: The attributes from an Opsgenie service response.
        :type attributes: OpsgenieServiceResponseAttributes

        :param id: The ID of the Opsgenie service.
        :type id: str

        :param type: Opsgenie service resource type.
        :type type: OpsgenieServiceType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.id = id
        self.type = type

    @classmethod
    def _from_openapi_data(cls, attributes, id, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(OpsgenieServiceResponseData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.id = id
        self.type = type
        return self
