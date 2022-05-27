# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityFilter(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_filter_attributes import SecurityFilterAttributes
        from datadog_api_client.v2.model.security_filter_type import SecurityFilterType

        return {
            "attributes": (SecurityFilterAttributes,),
            "id": (str,),
            "type": (SecurityFilterType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self, *args, **kwargs):
        """
        The security filter's properties.

        :param attributes: The object describing a security filter.
        :type attributes: SecurityFilterAttributes, optional

        :param id: The ID of the security filter.
        :type id: str, optional

        :param type: The type of the resource. The value should always be ``security_filters``.
        :type type: SecurityFilterType, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SecurityFilter, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
