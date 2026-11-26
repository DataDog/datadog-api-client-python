# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class WidgetTime(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param _from: Test-only generated schema for the dashboard versioning proof of concept.
        :type _from: float

        :param hide_incomplete_cost_data: Test-only generated schema for the dashboard versioning proof of concept.
        :type hide_incomplete_cost_data: bool, optional

        :param to: Test-only generated schema for the dashboard versioning proof of concept.
        :type to: float

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: WidgetNewFixedSpanType

        :param unit: Test-only generated schema for the dashboard versioning proof of concept.
        :type unit: str

        :param value: Test-only generated schema for the dashboard versioning proof of concept.
        :type value: float

        :param offset: Test-only generated schema for the dashboard versioning proof of concept.
        :type offset: float

        :param live_span: Test-only generated schema for the dashboard versioning proof of concept.
        :type live_span: LegacyLiveSpan
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
        from datadog_api_client.v1_20270101.model.widget_time20270101_one_of import WidgetTime20270101OneOf
        from datadog_api_client.v1_20270101.model.widget_time20270101_one_of4464103552 import (
            WidgetTime20270101OneOf4464103552,
        )
        from datadog_api_client.v1_20270101.model.widget_time20270101_one_of4464104512 import (
            WidgetTime20270101OneOf4464104512,
        )
        from datadog_api_client.v1_20270101.model.widget_time20270101_one_of4464105312 import (
            WidgetTime20270101OneOf4464105312,
        )
        from datadog_api_client.v1.model.widget_time20270101_one_of4464105952 import WidgetTime20270101OneOf4464105952
        from datadog_api_client.v1.model.empty_object import EmptyObject

        return {
            "oneOf": [
                WidgetTime20270101OneOf,
                WidgetTime20270101OneOf4464103552,
                WidgetTime20270101OneOf4464104512,
                WidgetTime20270101OneOf4464105312,
                WidgetTime20270101OneOf4464105952,
                EmptyObject,
            ],
        }
