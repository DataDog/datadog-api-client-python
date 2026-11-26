# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class WidgetLayout(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param height: Test-only generated schema for the dashboard versioning proof of concept.
        :type height: float, optional

        :param width: Test-only generated schema for the dashboard versioning proof of concept.
        :type width: float, optional

        :param x: Test-only generated schema for the dashboard versioning proof of concept.
        :type x: float

        :param y: Test-only generated schema for the dashboard versioning proof of concept.
        :type y: float

        :param parent: Test-only generated schema for the dashboard versioning proof of concept.
        :type parent: float, none_type, optional

        :param is_column_break: Test-only generated schema for the dashboard versioning proof of concept.
        :type is_column_break: bool, optional
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v1_20270101.model.free_layout import FreeLayout
        from datadog_api_client.v1_20270101.model.msl_widget_layout import MSLWidgetLayout
        from datadog_api_client.v1_20270101.model.msl_backend_widget_layout import MSLBackendWidgetLayout

        return {
            "oneOf": [
                FreeLayout,
                MSLWidgetLayout,
                MSLBackendWidgetLayout,
            ],
        }
