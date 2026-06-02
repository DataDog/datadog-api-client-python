# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AggregatedLowCacheHitRate(ModelNormal):
    validations = {
        "view_occurrences": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "avg_cache_hit_rate": (float,),
            "avg_resource_download_size_bytes": (int,),
            "fingerprint": (str,),
            "impact_score": (float,),
            "view_occurrences": (int,),
        }

    attribute_map = {
        "avg_cache_hit_rate": "avg_cache_hit_rate",
        "avg_resource_download_size_bytes": "avg_resource_download_size_bytes",
        "fingerprint": "fingerprint",
        "impact_score": "impact_score",
        "view_occurrences": "view_occurrences",
    }

    def __init__(
        self_,
        avg_cache_hit_rate: float,
        avg_resource_download_size_bytes: int,
        fingerprint: str,
        impact_score: float,
        view_occurrences: int,
        **kwargs,
    ):
        """
        Aggregated low cache hit rate detection at view level.

        :param avg_cache_hit_rate: Average cache hit rate across affected views.
        :type avg_cache_hit_rate: float

        :param avg_resource_download_size_bytes: Average total download size of uncached resources in bytes.
        :type avg_resource_download_size_bytes: int

        :param fingerprint: Unique fingerprint identifying this detection group.
        :type fingerprint: str

        :param impact_score: Impact score for this detection.
        :type impact_score: float

        :param view_occurrences: Number of sampled views where this detection occurred.
        :type view_occurrences: int
        """
        super().__init__(kwargs)

        self_.avg_cache_hit_rate = avg_cache_hit_rate
        self_.avg_resource_download_size_bytes = avg_resource_download_size_bytes
        self_.fingerprint = fingerprint
        self_.impact_score = impact_score
        self_.view_occurrences = view_occurrences
