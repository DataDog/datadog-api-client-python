# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MonitorFormulaAndFunctionAggregateAugmentedDataSource(ModelSimple):
    """
    Data source for aggregate augmented queries.

    :param value: If omitted defaults to "aggregate_augmented_query". Must be one of ["aggregate_augmented_query"].
    :type value: str
    """

    allowed_values = {
        "aggregate_augmented_query",
    }
    AGGREGATE_AUGMENTED_QUERY: ClassVar["MonitorFormulaAndFunctionAggregateAugmentedDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MonitorFormulaAndFunctionAggregateAugmentedDataSource.AGGREGATE_AUGMENTED_QUERY = (
    MonitorFormulaAndFunctionAggregateAugmentedDataSource("aggregate_augmented_query")
)
