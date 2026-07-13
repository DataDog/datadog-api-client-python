# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AWSMetricNameFiltersExcludeOnly(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "exclude_only": ([str],),
            "namespace": (str,),
        }

    attribute_map = {
        "exclude_only": "exclude_only",
        "namespace": "namespace",
    }

    def __init__(self_, exclude_only: List[str], namespace: str, **kwargs):
        """
        Exclude metric names matching one of these patterns for a single namespace.

        :param exclude_only: Exclude metric names matching one of these patterns.
        :type exclude_only: [str]

        :param namespace: The AWS CloudWatch namespace to which this metric name filter applies.
        :type namespace: str
        """
        super().__init__(kwargs)

        self_.exclude_only = exclude_only
        self_.namespace = namespace
