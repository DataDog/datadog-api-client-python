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
            "defaults": ([str],),
            "name": (str,),
            "prefix": (str, none_type),
        }

    attribute_map = {
        "available_values": "available_values",
        "default": "default",
        "defaults": "defaults",
        "name": "name",
        "prefix": "prefix",
    }

    def __init__(self_, name, *args, **kwargs):
        """
        Template variable.

        :param available_values: The list of values that the template variable drop-down is limited to.
        :type available_values: [str], none_type, optional

        :param default: (deprecated) The default value for the template variable on dashboard load. Cannot be used in conjunction with ``defaults``. **Deprecated**.
        :type default: str, none_type, optional

        :param defaults: One or many default values for template variables on load. If more than one default is specified, they will be unioned together with ``OR``. Cannot be used in conjunction with ``default``.
        :type defaults: [str], optional

        :param name: The name of the variable.
        :type name: str

        :param prefix: The tag prefix associated with the variable. Only tags with this prefix appear in the variable drop-down.
        :type prefix: str, none_type, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.name = name
