# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class TagPolicyScoreAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "score": (float, none_type),
            "ts_end": (int,),
            "ts_start": (int,),
            "version": (int,),
        }

    attribute_map = {
        "score": "score",
        "ts_end": "ts_end",
        "ts_start": "ts_start",
        "version": "version",
    }

    def __init__(self_, score: Union[float, none_type], ts_end: int, ts_start: int, version: int, **kwargs):
        """
        Attributes of a tag policy compliance score.

        :param score: The compliance score for the policy over the requested time window, as a percentage
            between 0 and 100. ``null`` indicates that no relevant telemetry was found.
        :type score: float, none_type

        :param ts_end: End of the time window the score was computed over, as a Unix timestamp in milliseconds.
        :type ts_end: int

        :param ts_start: Start of the time window the score was computed over, as a Unix timestamp in milliseconds.
        :type ts_start: int

        :param version: The version of the tag policy that the score was computed against.
        :type version: int
        """
        super().__init__(kwargs)

        self_.score = score
        self_.ts_end = ts_end
        self_.ts_start = ts_start
        self_.version = version
