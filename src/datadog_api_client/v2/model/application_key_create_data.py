# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ApplicationKeyCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.application_key_create_attributes import ApplicationKeyCreateAttributes
        from datadog_api_client.v2.model.application_keys_type import ApplicationKeysType

        return {
            "attributes": (ApplicationKeyCreateAttributes,),
            "type": (ApplicationKeysType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self, attributes, type, *args, **kwargs):
        """
        Object used to create an application key.

        :param attributes: Attributes used to create an application Key.
        :type attributes: ApplicationKeyCreateAttributes

        :param type: Application Keys resource type.
        :type type: ApplicationKeysType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.type = type

    @classmethod
    def _from_openapi_data(cls, attributes, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ApplicationKeyCreateData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.type = type
        return self
