# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelComposed,
    cached_property,
)


class SunburstWidgetLegend(ModelComposed):

    validations = {}

    @cached_property
    def openapi_types():
        return {}

    def __init__(self, *args, **kwargs):
        """
        Configuration of the legend.

        :param type: Whether or not to show a table legend.
        :type type: SunburstWidgetLegendTableType

        :param hide_percent: Whether to hide the percentages of the groups.
        :type hide_percent: bool, optional

        :param hide_value: Whether to hide the values of the groups.
        :type hide_value: bool, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SunburstWidgetLegend, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        return {
            "anyOf": [],
            "allOf": [],
            "oneOf": [],
        }
