# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CommitmentsQueryDefinitionDataSource(ModelSimple):
    """
    The data source of the query.

    :param value: Must be one of ["cloud_cost", "metrics"].
    :type value: str
    """

    allowed_values = {
        "cloud_cost",
        "metrics",
    }
    CLOUD_COST: ClassVar["CommitmentsQueryDefinitionDataSource"]
    METRICS: ClassVar["CommitmentsQueryDefinitionDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CommitmentsQueryDefinitionDataSource.CLOUD_COST = CommitmentsQueryDefinitionDataSource("cloud_cost")
CommitmentsQueryDefinitionDataSource.METRICS = CommitmentsQueryDefinitionDataSource("metrics")
