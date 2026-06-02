# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AggregatedSlowFCPHighBytes(ModelNormal):
    validations = {
        "view_occurrences": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "avg_bytes_before_fcp_bytes": (int,),
            "avg_first_contentful_paint_ms": (int,),
            "avg_resource_count_before_fcp": (int,),
            "fingerprint": (str,),
            "impact_score": (float,),
            "platform": (str,),
            "view_occurrences": (int,),
        }

    attribute_map = {
        "avg_bytes_before_fcp_bytes": "avg_bytes_before_fcp_bytes",
        "avg_first_contentful_paint_ms": "avg_first_contentful_paint_ms",
        "avg_resource_count_before_fcp": "avg_resource_count_before_fcp",
        "fingerprint": "fingerprint",
        "impact_score": "impact_score",
        "platform": "platform",
        "view_occurrences": "view_occurrences",
    }

    def __init__(
        self_,
        avg_bytes_before_fcp_bytes: int,
        avg_first_contentful_paint_ms: int,
        avg_resource_count_before_fcp: int,
        fingerprint: str,
        impact_score: float,
        platform: str,
        view_occurrences: int,
        **kwargs,
    ):
        """
        Aggregated slow first contentful paint with high byte count detection.

        :param avg_bytes_before_fcp_bytes: Average total bytes loaded before first contentful paint.
        :type avg_bytes_before_fcp_bytes: int

        :param avg_first_contentful_paint_ms: Average first contentful paint time in milliseconds.
        :type avg_first_contentful_paint_ms: int

        :param avg_resource_count_before_fcp: Average number of resources loaded before first contentful paint.
        :type avg_resource_count_before_fcp: int

        :param fingerprint: Unique fingerprint identifying this detection group.
        :type fingerprint: str

        :param impact_score: Impact score for this detection.
        :type impact_score: float

        :param platform: Platform identifier for the affected views.
        :type platform: str

        :param view_occurrences: Number of sampled views where this detection occurred.
        :type view_occurrences: int
        """
        super().__init__(kwargs)

        self_.avg_bytes_before_fcp_bytes = avg_bytes_before_fcp_bytes
        self_.avg_first_contentful_paint_ms = avg_first_contentful_paint_ms
        self_.avg_resource_count_before_fcp = avg_resource_count_before_fcp
        self_.fingerprint = fingerprint
        self_.impact_score = impact_score
        self_.platform = platform
        self_.view_occurrences = view_occurrences
