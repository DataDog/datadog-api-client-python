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


class AggregatedUncompressedResource(ModelNormal):
    validations = {
        "instance_count": {
            "inclusive_maximum": 2147483647,
        },
        "view_occurrences": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "avg_body_size": (int,),
            "avg_duration": (int,),
            "fingerprint": (str,),
            "impact_score": (float,),
            "instance_count": (int,),
            "provider_type": (str, none_type),
            "render_blocking": (str, none_type),
            "resource_type": (str,),
            "url_path_group": (str,),
            "view_occurrences": (int,),
        }

    attribute_map = {
        "avg_body_size": "avg_body_size",
        "avg_duration": "avg_duration",
        "fingerprint": "fingerprint",
        "impact_score": "impact_score",
        "instance_count": "instance_count",
        "provider_type": "provider_type",
        "render_blocking": "render_blocking",
        "resource_type": "resource_type",
        "url_path_group": "url_path_group",
        "view_occurrences": "view_occurrences",
    }

    def __init__(
        self_,
        avg_body_size: int,
        avg_duration: int,
        fingerprint: str,
        impact_score: float,
        instance_count: int,
        provider_type: Union[str, none_type],
        render_blocking: Union[str, none_type],
        resource_type: str,
        url_path_group: str,
        view_occurrences: int,
        **kwargs,
    ):
        """
        Aggregated uncompressed resource detection grouped by URL path.

        :param avg_body_size: Average uncompressed body size in bytes.
        :type avg_body_size: int

        :param avg_duration: Average resource loading duration in nanoseconds.
        :type avg_duration: int

        :param fingerprint: Unique fingerprint identifying this detection group.
        :type fingerprint: str

        :param impact_score: Impact score combining view frequency and resource size.
        :type impact_score: float

        :param instance_count: Total number of detection instances across sampled views.
        :type instance_count: int

        :param provider_type: CDN or hosting provider type for the resource.
        :type provider_type: str, none_type

        :param render_blocking: Whether the resource is render-blocking.
        :type render_blocking: str, none_type

        :param resource_type: Type of the resource (JS, CSS, image, fetch, and so on).
        :type resource_type: str

        :param url_path_group: Normalized URL path pattern for the uncompressed resource.
        :type url_path_group: str

        :param view_occurrences: Number of sampled views where this detection occurred.
        :type view_occurrences: int
        """
        super().__init__(kwargs)

        self_.avg_body_size = avg_body_size
        self_.avg_duration = avg_duration
        self_.fingerprint = fingerprint
        self_.impact_score = impact_score
        self_.instance_count = instance_count
        self_.provider_type = provider_type
        self_.render_blocking = render_blocking
        self_.resource_type = resource_type
        self_.url_path_group = url_path_group
        self_.view_occurrences = view_occurrences
