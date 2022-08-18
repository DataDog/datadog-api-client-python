# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RUMApplicationCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "type": (str,),
        }

    attribute_map = {
        "name": "name",
        "type": "type",
    }

    def __init__(self, name, *args, **kwargs):
        """
        RUM application creation attributes.

        :param name: Name of the RUM application.
        :type name: str

        :param type: Type of the RUM application. Supported values are ``browser`` , ``ios`` , ``android`` , ``react-native`` , ``flutter``.
        :type type: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.name = name

    @classmethod
    def _from_openapi_data(cls, name, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(RUMApplicationCreateAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.name = name
        return self
