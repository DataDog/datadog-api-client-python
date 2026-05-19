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
    from datadog_api_client.v2.model.case_aggregate_response_data import CaseAggregateResponseData


class CaseAggregateResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_aggregate_response_data import CaseAggregateResponseData

        return {
            "data": (CaseAggregateResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CaseAggregateResponseData, **kwargs):
        """
        Response containing aggregated case counts grouped by the requested fields.

        :param data: Data object containing the aggregation results, including total count and per-group breakdowns.
        :type data: CaseAggregateResponseData
        """
        super().__init__(kwargs)

        self_.data = data
