# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelComposed,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.notebook_relative_time import NotebookRelativeTime
    from datadog_api_client.v1.model.notebook_absolute_time import NotebookAbsoluteTime

    globals()["NotebookRelativeTime"] = NotebookRelativeTime
    globals()["NotebookAbsoluteTime"] = NotebookAbsoluteTime


class NotebookGlobalTime(ModelComposed):

    validations = {}

    @cached_property
    def openapi_types():
        return {}

    def __init__(self, *args, **kwargs):
        """
        Notebook global timeframe.

        :param live_span: The available timeframes depend on the widget you are using.
        :type live_span: WidgetLiveSpan

        :param end: The end time.
        :type end: datetime

        :param live: Indicates whether the timeframe should be shifted to end at the current time.
        :type live: bool, optional

        :param start: The start time.
        :type start: datetime
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(NotebookGlobalTime, cls)._from_openapi_data(kwargs)

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
        lazy_import()
        return {
            "anyOf": [],
            "allOf": [],
            "oneOf": [
                NotebookRelativeTime,
                NotebookAbsoluteTime,
            ],
        }
