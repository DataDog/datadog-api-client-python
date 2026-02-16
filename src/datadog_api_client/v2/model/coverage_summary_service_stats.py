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


class CoverageSummaryServiceStats(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "evaluated_flags_count": (int,),
            "evaluated_reports_count": (int,),
            "patch_coverage": (float, none_type),
            "total_coverage": (float, none_type),
        }

    attribute_map = {
        "evaluated_flags_count": "evaluated_flags_count",
        "evaluated_reports_count": "evaluated_reports_count",
        "patch_coverage": "patch_coverage",
        "total_coverage": "total_coverage",
    }

    def __init__(
        self_,
        evaluated_flags_count: Union[int, UnsetType] = unset,
        evaluated_reports_count: Union[int, UnsetType] = unset,
        patch_coverage: Union[float, none_type, UnsetType] = unset,
        total_coverage: Union[float, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Coverage statistics for a specific service.

        :param evaluated_flags_count: Number of coverage flags evaluated for the service.
        :type evaluated_flags_count: int, optional

        :param evaluated_reports_count: Number of coverage reports evaluated for the service.
        :type evaluated_reports_count: int, optional

        :param patch_coverage: Patch coverage percentage for the service.
        :type patch_coverage: float, none_type, optional

        :param total_coverage: Total coverage percentage for the service.
        :type total_coverage: float, none_type, optional
        """
        if evaluated_flags_count is not unset:
            kwargs["evaluated_flags_count"] = evaluated_flags_count
        if evaluated_reports_count is not unset:
            kwargs["evaluated_reports_count"] = evaluated_reports_count
        if patch_coverage is not unset:
            kwargs["patch_coverage"] = patch_coverage
        if total_coverage is not unset:
            kwargs["total_coverage"] = total_coverage
        super().__init__(kwargs)
