# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AggregatedHighFrozenFrameRate(ModelNormal):
    validations = {
        "view_occurrences": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "avg_frozen_frame_rate": (float,),
            "avg_segment_duration": (int,),
            "avg_total_frozen_duration": (int,),
            "fingerprint": (str,),
            "impact_score": (float,),
            "view_occurrences": (int,),
        }

    attribute_map = {
        "avg_frozen_frame_rate": "avg_frozen_frame_rate",
        "avg_segment_duration": "avg_segment_duration",
        "avg_total_frozen_duration": "avg_total_frozen_duration",
        "fingerprint": "fingerprint",
        "impact_score": "impact_score",
        "view_occurrences": "view_occurrences",
    }

    def __init__(
        self_,
        avg_frozen_frame_rate: float,
        avg_segment_duration: int,
        avg_total_frozen_duration: int,
        fingerprint: str,
        impact_score: float,
        view_occurrences: int,
        **kwargs,
    ):
        """
        Aggregated high frozen frame rate detection at view level.

        :param avg_frozen_frame_rate: Average frozen frame rate as a fraction of total frames.
        :type avg_frozen_frame_rate: float

        :param avg_segment_duration: Average segment duration in nanoseconds.
        :type avg_segment_duration: int

        :param avg_total_frozen_duration: Average total frozen duration in nanoseconds.
        :type avg_total_frozen_duration: int

        :param fingerprint: Unique fingerprint identifying this detection group.
        :type fingerprint: str

        :param impact_score: Impact score for this detection.
        :type impact_score: float

        :param view_occurrences: Number of sampled views where this detection occurred.
        :type view_occurrences: int
        """
        super().__init__(kwargs)

        self_.avg_frozen_frame_rate = avg_frozen_frame_rate
        self_.avg_segment_duration = avg_segment_duration
        self_.avg_total_frozen_duration = avg_total_frozen_duration
        self_.fingerprint = fingerprint
        self_.impact_score = impact_score
        self_.view_occurrences = view_occurrences
