# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.branch_coverage_summary_request_attributes import (
        BranchCoverageSummaryRequestAttributes,
    )
    from datadog_api_client.v2.model.branch_coverage_summary_request_type import BranchCoverageSummaryRequestType


class BranchCoverageSummaryRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.branch_coverage_summary_request_attributes import (
            BranchCoverageSummaryRequestAttributes,
        )
        from datadog_api_client.v2.model.branch_coverage_summary_request_type import BranchCoverageSummaryRequestType

        return {
            "attributes": (BranchCoverageSummaryRequestAttributes,),
            "type": (BranchCoverageSummaryRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: BranchCoverageSummaryRequestAttributes, type: BranchCoverageSummaryRequestType, **kwargs
    ):
        """
        Data object for branch summary request.

        :param attributes: Attributes for requesting code coverage summary for a branch.
        :type attributes: BranchCoverageSummaryRequestAttributes

        :param type: JSON:API type for branch coverage summary request. The value must always be ``ci_app_coverage_branch_summary_request``.
        :type type: BranchCoverageSummaryRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
