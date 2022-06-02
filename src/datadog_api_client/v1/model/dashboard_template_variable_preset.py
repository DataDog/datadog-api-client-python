# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DashboardTemplateVariablePreset(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.dashboard_template_variable_preset_value import (
            DashboardTemplateVariablePresetValue,
        )

        return {
            "name": (str,),
            "template_variables": ([DashboardTemplateVariablePresetValue],),
        }

    attribute_map = {
        "name": "name",
        "template_variables": "template_variables",
    }

    def __init__(self, *args, **kwargs):
        """
        Template variables saved views.

        :param name: The name of the variable.
        :type name: str, optional

        :param template_variables: List of variables.
        :type template_variables: [DashboardTemplateVariablePresetValue], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(DashboardTemplateVariablePreset, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
