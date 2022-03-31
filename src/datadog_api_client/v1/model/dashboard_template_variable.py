# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class DashboardTemplateVariable(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "available_values": ([str], none_type),
            "default": (str, none_type),
            "name": (str,),
            "prefix": (str, none_type),
        }

    attribute_map = {
        "available_values": "available_values",
        "default": "default",
        "name": "name",
        "prefix": "prefix",
    }

    def __init__(self, name, *args, **kwargs):
        """
        Template variable.

        :param available_values: The list of values that the template variable drop-down is limited to.
        :type available_values: [str], none_type, optional

        :param default: The default value for the template variable on dashboard load.
        :type default: str, none_type, optional

        :param name: The name of the variable.
        :type name: str

        :param prefix: The tag prefix associated with the variable. Only tags with this prefix appear in the variable drop-down.
        :type prefix: str, none_type, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.name = name

    @classmethod
    def _from_openapi_data(cls, name, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(DashboardTemplateVariable, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.name = name
        return self
