# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityFilterUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_filter_update_attributes import SecurityFilterUpdateAttributes
        from datadog_api_client.v2.model.security_filter_type import SecurityFilterType

        return {
            "attributes": (SecurityFilterUpdateAttributes,),
            "type": (SecurityFilterType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self, attributes, type, *args, **kwargs):
        """
        The new security filter properties.

        :param attributes: The security filters properties to be updated.
        :type attributes: SecurityFilterUpdateAttributes

        :param type: The type of the resource. The value should always be ``security_filters``.
        :type type: SecurityFilterType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.type = type

    @classmethod
    def _from_openapi_data(cls, attributes, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SecurityFilterUpdateData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.type = type
        return self
