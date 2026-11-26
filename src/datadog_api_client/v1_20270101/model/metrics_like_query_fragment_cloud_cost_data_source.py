# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MetricsLikeQueryFragmentCloudCostDataSource(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: If omitted defaults to "cloud_cost". Must be one of ["cloud_cost"].
    :type value: str
    """

    allowed_values = {
        "cloud_cost",
    }
    CLOUD_COST: ClassVar["MetricsLikeQueryFragmentCloudCostDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MetricsLikeQueryFragmentCloudCostDataSource.CLOUD_COST = MetricsLikeQueryFragmentCloudCostDataSource("cloud_cost")
