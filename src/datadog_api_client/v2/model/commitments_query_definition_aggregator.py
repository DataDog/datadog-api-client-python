# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CommitmentsQueryDefinitionAggregator(ModelSimple):
    """
    The reducer a scalar widget applies to the query.

    :param value: Must be one of ["sum", "avg", "min", "max"].
    :type value: str
    """

    allowed_values = {
        "sum",
        "avg",
        "min",
        "max",
    }
    SUM: ClassVar["CommitmentsQueryDefinitionAggregator"]
    AVG: ClassVar["CommitmentsQueryDefinitionAggregator"]
    MIN: ClassVar["CommitmentsQueryDefinitionAggregator"]
    MAX: ClassVar["CommitmentsQueryDefinitionAggregator"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CommitmentsQueryDefinitionAggregator.SUM = CommitmentsQueryDefinitionAggregator("sum")
CommitmentsQueryDefinitionAggregator.AVG = CommitmentsQueryDefinitionAggregator("avg")
CommitmentsQueryDefinitionAggregator.MIN = CommitmentsQueryDefinitionAggregator("min")
CommitmentsQueryDefinitionAggregator.MAX = CommitmentsQueryDefinitionAggregator("max")
