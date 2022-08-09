# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RUMApplication(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_application_attributes import RUMApplicationAttributes
        from datadog_api_client.v2.model.rum_application_type import RUMApplicationType

        return {
            "attributes": (RUMApplicationAttributes,),
            "id": (str,),
            "type": (RUMApplicationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self, attributes, id, type, *args, **kwargs):
        """
        RUM application.

        :param attributes: RUM application attributes.
        :type attributes: RUMApplicationAttributes

        :param id: RUM application ID.
        :type id: str

        :param type: RUM application response type.
        :type type: RUMApplicationType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.id = id
        self.type = type

    @classmethod
    def _from_openapi_data(cls, attributes, id, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(RUMApplication, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.id = id
        self.type = type
        return self
