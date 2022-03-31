# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DashboardTemplateVariablePresetValue(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "value": (str,),
        }

    attribute_map = {
        "name": "name",
        "value": "value",
    }

    def __init__(self, *args, **kwargs):
        """
        Template variables saved views.

        :param name: The name of the variable.
        :type name: str, optional

        :param value: The value of the template variable within the saved view.
        :type value: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(DashboardTemplateVariablePresetValue, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
