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


class CsmCoverageAnalysis(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "configured_resources_count": (int,),
            "coverage": (float,),
            "partially_configured_resources_count": (int,),
            "total_resources_count": (int,),
        }

    attribute_map = {
        "configured_resources_count": "configured_resources_count",
        "coverage": "coverage",
        "partially_configured_resources_count": "partially_configured_resources_count",
        "total_resources_count": "total_resources_count",
    }

    def __init__(
        self_,
        configured_resources_count: Union[int, UnsetType] = unset,
        coverage: Union[float, UnsetType] = unset,
        partially_configured_resources_count: Union[int, UnsetType] = unset,
        total_resources_count: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        CSM Coverage Analysis.

        :param configured_resources_count: The number of fully configured resources.
        :type configured_resources_count: int, optional

        :param coverage: The coverage percentage.
        :type coverage: float, optional

        :param partially_configured_resources_count: The number of partially configured resources.
        :type partially_configured_resources_count: int, optional

        :param total_resources_count: The total number of resources.
        :type total_resources_count: int, optional
        """
        if configured_resources_count is not unset:
            kwargs["configured_resources_count"] = configured_resources_count
        if coverage is not unset:
            kwargs["coverage"] = coverage
        if partially_configured_resources_count is not unset:
            kwargs["partially_configured_resources_count"] = partially_configured_resources_count
        if total_resources_count is not unset:
            kwargs["total_resources_count"] = total_resources_count
        super().__init__(kwargs)
