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
    from datadog_api_client.v2.model.pr_coverage_summary_request_data import PRCoverageSummaryRequestData


class PRCoverageSummaryRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.pr_coverage_summary_request_data import PRCoverageSummaryRequestData

        return {
            "data": (PRCoverageSummaryRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: PRCoverageSummaryRequestData, **kwargs):
        """
        Request object for getting code coverage summary for a pull request.

        :param data: Data object for PR summary request.
        :type data: PRCoverageSummaryRequestData
        """
        super().__init__(kwargs)

        self_.data = data
