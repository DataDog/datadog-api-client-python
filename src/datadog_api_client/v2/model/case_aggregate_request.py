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
    from datadog_api_client.v2.model.case_aggregate_request_data import CaseAggregateRequestData


class CaseAggregateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_aggregate_request_data import CaseAggregateRequestData

        return {
            "data": (CaseAggregateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CaseAggregateRequestData, **kwargs):
        """
        Request payload for aggregating case counts with grouping. Use this to get faceted breakdowns of cases (for example, count of cases grouped by priority and status).

        :param data: Data object wrapping the aggregation query type and attributes.
        :type data: CaseAggregateRequestData
        """
        super().__init__(kwargs)

        self_.data = data
