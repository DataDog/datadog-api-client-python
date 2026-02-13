# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class BranchCoverageSummaryRequestType(ModelSimple):
    """
    JSON:API type for branch coverage summary request. The value must always be `ci_app_coverage_branch_summary_request`.

    :param value: If omitted defaults to "ci_app_coverage_branch_summary_request". Must be one of ["ci_app_coverage_branch_summary_request"].
    :type value: str
    """

    allowed_values = {
        "ci_app_coverage_branch_summary_request",
    }
    CI_APP_COVERAGE_BRANCH_SUMMARY_REQUEST: ClassVar["BranchCoverageSummaryRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


BranchCoverageSummaryRequestType.CI_APP_COVERAGE_BRANCH_SUMMARY_REQUEST = BranchCoverageSummaryRequestType(
    "ci_app_coverage_branch_summary_request"
)
