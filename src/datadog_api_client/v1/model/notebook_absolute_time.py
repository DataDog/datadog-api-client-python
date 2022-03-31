# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class NotebookAbsoluteTime(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "end": (datetime,),
            "live": (bool,),
            "start": (datetime,),
        }

    attribute_map = {
        "end": "end",
        "live": "live",
        "start": "start",
    }

    def __init__(self, end, start, *args, **kwargs):
        """
        Absolute timeframe.

        :param end: The end time.
        :type end: datetime

        :param live: Indicates whether the timeframe should be shifted to end at the current time.
        :type live: bool, optional

        :param start: The start time.
        :type start: datetime
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.end = end
        self.start = start

    @classmethod
    def _from_openapi_data(cls, end, start, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(NotebookAbsoluteTime, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.end = end
        self.start = start
        return self
