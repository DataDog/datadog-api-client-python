# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MonitorFormulaAndFunctionAggregateFilteredDataSource(ModelSimple):
    """
    Data source for aggregate filtered queries.

    :param value: If omitted defaults to "aggregate_filtered_query". Must be one of ["aggregate_filtered_query"].
    :type value: str
    """

    allowed_values = {
        "aggregate_filtered_query",
    }
    AGGREGATE_FILTERED_QUERY: ClassVar["MonitorFormulaAndFunctionAggregateFilteredDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MonitorFormulaAndFunctionAggregateFilteredDataSource.AGGREGATE_FILTERED_QUERY = (
    MonitorFormulaAndFunctionAggregateFilteredDataSource("aggregate_filtered_query")
)
