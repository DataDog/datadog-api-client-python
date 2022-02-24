# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


class WidgetStyle(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "palette": (str,),
        }

    attribute_map = {
        "palette": "palette",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Widget style definition.

        :param palette: Color palette to apply to the widget.
        :type palette: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(WidgetStyle, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
