# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AggregatedLongTasksRequestType(ModelSimple):
    """
    The JSON:API type for aggregated long tasks requests.

    :param value: If omitted defaults to "aggregated_long_tasks". Must be one of ["aggregated_long_tasks"].
    :type value: str
    """

    allowed_values = {
        "aggregated_long_tasks",
    }
    AGGREGATED_LONG_TASKS: ClassVar["AggregatedLongTasksRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AggregatedLongTasksRequestType.AGGREGATED_LONG_TASKS = AggregatedLongTasksRequestType("aggregated_long_tasks")
