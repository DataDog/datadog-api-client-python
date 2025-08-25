# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class Cpu(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "max": (int,),
            "p75": (int,),
            "p95": (int,),
        }

    attribute_map = {
        "max": "max",
        "p75": "p75",
        "p95": "p95",
    }

    def __init__(
        self_,
        max: Union[int, UnsetType] = unset,
        p75: Union[int, UnsetType] = unset,
        p95: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        CPU usage statistics derived from historical Spark job metrics. Provides multiple estimates so users can choose between conservative and cost-saving risk profiles.

        :param max: Maximum CPU usage observed for the job, expressed in millicores. This represents the upper bound of usage.
        :type max: int, optional

        :param p75: 75th percentile of CPU usage (millicores). Represents a cost-saving configuration while covering most workloads.
        :type p75: int, optional

        :param p95: 95th percentile of CPU usage (millicores). Balances performance and cost, providing a safer margin than p75.
        :type p95: int, optional
        """
        if max is not unset:
            kwargs["max"] = max
        if p75 is not unset:
            kwargs["p75"] = p75
        if p95 is not unset:
            kwargs["p95"] = p95
        super().__init__(kwargs)
