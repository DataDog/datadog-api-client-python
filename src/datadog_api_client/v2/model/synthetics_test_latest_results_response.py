# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.synthetics_test_result_summary_data import SyntheticsTestResultSummaryData
    from datadog_api_client.v2.model.synthetics_test_result_included_item import SyntheticsTestResultIncludedItem


class SyntheticsTestLatestResultsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_summary_data import SyntheticsTestResultSummaryData
        from datadog_api_client.v2.model.synthetics_test_result_included_item import SyntheticsTestResultIncludedItem

        return {
            "data": ([SyntheticsTestResultSummaryData],),
            "included": ([SyntheticsTestResultIncludedItem],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: Union[List[SyntheticsTestResultSummaryData], UnsetType] = unset,
        included: Union[List[SyntheticsTestResultIncludedItem], UnsetType] = unset,
        **kwargs,
    ):
        """
        Response object for a Synthetic test's latest result summaries.

        :param data: Array of Synthetic test result summaries.
        :type data: [SyntheticsTestResultSummaryData], optional

        :param included: Array of included related resources, such as the test definition.
        :type included: [SyntheticsTestResultIncludedItem], optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)
