# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class NotebookRelativeTime(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_live_span import WidgetLiveSpan

        return {
            "live_span": (WidgetLiveSpan,),
        }

    attribute_map = {
        "live_span": "live_span",
    }

    def __init__(self, live_span, *args, **kwargs):
        """
        Relative timeframe.

        :param live_span: The available timeframes depend on the widget you are using.
        :type live_span: WidgetLiveSpan
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.live_span = live_span

    @classmethod
    def _from_openapi_data(cls, live_span, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(NotebookRelativeTime, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.live_span = live_span
        return self
