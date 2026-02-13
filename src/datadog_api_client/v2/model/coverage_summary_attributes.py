# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.coverage_summary_codeowner_stats import CoverageSummaryCodeownerStats
    from datadog_api_client.v2.model.coverage_summary_service_stats import CoverageSummaryServiceStats


class CoverageSummaryAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.coverage_summary_codeowner_stats import CoverageSummaryCodeownerStats
        from datadog_api_client.v2.model.coverage_summary_service_stats import CoverageSummaryServiceStats

        return {
            "codeowners": ({str: (CoverageSummaryCodeownerStats,)}, none_type),
            "evaluated_flags_count": (int,),
            "evaluated_reports_count": (int,),
            "patch_coverage": (float, none_type),
            "services": ({str: (CoverageSummaryServiceStats,)}, none_type),
            "total_coverage": (float, none_type),
        }

    attribute_map = {
        "codeowners": "codeowners",
        "evaluated_flags_count": "evaluated_flags_count",
        "evaluated_reports_count": "evaluated_reports_count",
        "patch_coverage": "patch_coverage",
        "services": "services",
        "total_coverage": "total_coverage",
    }

    def __init__(
        self_,
        codeowners: Union[Dict[str, CoverageSummaryCodeownerStats], none_type, UnsetType] = unset,
        evaluated_flags_count: Union[int, UnsetType] = unset,
        evaluated_reports_count: Union[int, UnsetType] = unset,
        patch_coverage: Union[float, none_type, UnsetType] = unset,
        services: Union[Dict[str, CoverageSummaryServiceStats], none_type, UnsetType] = unset,
        total_coverage: Union[float, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes object for code coverage summary response.

        :param codeowners: Coverage statistics broken down by code owner.
        :type codeowners: {str: (CoverageSummaryCodeownerStats,)}, none_type, optional

        :param evaluated_flags_count: Total number of coverage flags evaluated.
        :type evaluated_flags_count: int, optional

        :param evaluated_reports_count: Total number of coverage reports evaluated.
        :type evaluated_reports_count: int, optional

        :param patch_coverage: Overall patch coverage percentage.
        :type patch_coverage: float, none_type, optional

        :param services: Coverage statistics broken down by service.
        :type services: {str: (CoverageSummaryServiceStats,)}, none_type, optional

        :param total_coverage: Overall total coverage percentage.
        :type total_coverage: float, none_type, optional
        """
        if codeowners is not unset:
            kwargs["codeowners"] = codeowners
        if evaluated_flags_count is not unset:
            kwargs["evaluated_flags_count"] = evaluated_flags_count
        if evaluated_reports_count is not unset:
            kwargs["evaluated_reports_count"] = evaluated_reports_count
        if patch_coverage is not unset:
            kwargs["patch_coverage"] = patch_coverage
        if services is not unset:
            kwargs["services"] = services
        if total_coverage is not unset:
            kwargs["total_coverage"] = total_coverage
        super().__init__(kwargs)
