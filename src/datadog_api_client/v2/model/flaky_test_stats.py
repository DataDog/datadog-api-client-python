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


class FlakyTestStats(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "failure_rate_pct": (float, none_type),
        }

    attribute_map = {
        "failure_rate_pct": "failure_rate_pct",
    }

    def __init__(self_, failure_rate_pct: Union[float, none_type, UnsetType] = unset, **kwargs):
        """
        Test statistics for the flaky test.

        :param failure_rate_pct: The failure rate percentage of the test for the past 7 days. This is the number of failed test runs divided by the total number of test runs (excluding skipped test runs).
        :type failure_rate_pct: float, none_type, optional
        """
        if failure_rate_pct is not unset:
            kwargs["failure_rate_pct"] = failure_rate_pct
        super().__init__(kwargs)
