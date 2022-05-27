# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ApplicationKeyUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.application_key_update_attributes import ApplicationKeyUpdateAttributes
        from datadog_api_client.v2.model.application_keys_type import ApplicationKeysType

        return {
            "attributes": (ApplicationKeyUpdateAttributes,),
            "id": (str,),
            "type": (ApplicationKeysType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self, attributes, id, type, *args, **kwargs):
        """
        Object used to update an application key.

        :param attributes: Attributes used to update an application Key.
        :type attributes: ApplicationKeyUpdateAttributes

        :param id: ID of the application key.
        :type id: str

        :param type: Application Keys resource type.
        :type type: ApplicationKeysType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.id = id
        self.type = type

    @classmethod
    def _from_openapi_data(cls, attributes, id, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ApplicationKeyUpdateData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.id = id
        self.type = type
        return self
