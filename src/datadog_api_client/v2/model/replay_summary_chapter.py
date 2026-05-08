# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ReplaySummaryChapter(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "end_ms": (int,),
            "start_ms": (int,),
            "text": (str,),
        }

    attribute_map = {
        "end_ms": "end_ms",
        "start_ms": "start_ms",
        "text": "text",
    }

    def __init__(self_, end_ms: int, start_ms: int, text: str, **kwargs):
        """
        A chapter within a RUM replay summary, representing a distinct segment of user activity.

        :param end_ms: End time of the chapter in milliseconds.
        :type end_ms: int

        :param start_ms: Start time of the chapter in milliseconds.
        :type start_ms: int

        :param text: Description of user activity during this chapter.
        :type text: str
        """
        super().__init__(kwargs)

        self_.end_ms = end_ms
        self_.start_ms = start_ms
        self_.text = text
