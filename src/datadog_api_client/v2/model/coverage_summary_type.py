# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CoverageSummaryType(ModelSimple):
    """
    JSON:API type for coverage summary response. The value must always be `ci_app_coverage_summary`.

    :param value: If omitted defaults to "ci_app_coverage_summary". Must be one of ["ci_app_coverage_summary"].
    :type value: str
    """

    allowed_values = {
        "ci_app_coverage_summary",
    }
    CI_APP_COVERAGE_SUMMARY: ClassVar["CoverageSummaryType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CoverageSummaryType.CI_APP_COVERAGE_SUMMARY = CoverageSummaryType("ci_app_coverage_summary")
