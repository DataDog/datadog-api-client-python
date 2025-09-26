# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class FlakyTestPipelineStats(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "failed_pipelines": (int, none_type),
            "total_lost_time_ms": (int, none_type),
        }

    attribute_map = {
        "failed_pipelines": "failed_pipelines",
        "total_lost_time_ms": "total_lost_time_ms",
    }

    def __init__(
        self_,
        failed_pipelines: Union[int, none_type, UnsetType] = unset,
        total_lost_time_ms: Union[int, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        CI pipeline related statistics for the flaky test. This information is only available if test runs are associated with CI pipeline events from CI Visibility.

        :param failed_pipelines: The number of pipelines that failed due to this test for the past 7 days. This is computed as the sum of failed CI pipeline events associated with test runs where the flaky test failed.
        :type failed_pipelines: int, none_type, optional

        :param total_lost_time_ms: The total time lost by CI pipelines due to this flaky test in milliseconds. This is computed as the sum of the duration of failed CI pipeline events associated with test runs where the flaky test failed.
        :type total_lost_time_ms: int, none_type, optional
        """
        if failed_pipelines is not unset:
            kwargs["failed_pipelines"] = failed_pipelines
        if total_lost_time_ms is not unset:
            kwargs["total_lost_time_ms"] = total_lost_time_ms
        super().__init__(kwargs)
