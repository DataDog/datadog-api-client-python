# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LLMObsContentBlockTimeFrame(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "end": (int,),
            "start": (int,),
        }

    attribute_map = {
        "end": "end",
        "start": "start",
    }

    def __init__(self_, end: int, start: int, **kwargs):
        """
        Unix-millis time range used by chart blocks.

        :param end: End of the range, in Unix milliseconds.
        :type end: int

        :param start: Start of the range, in Unix milliseconds.
        :type start: int
        """
        super().__init__(kwargs)

        self_.end = end
        self_.start = start
