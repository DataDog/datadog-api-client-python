# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SampleLogGenerationSubscriptionsStatusFilter(ModelSimple):
    """
    Filter that controls whether to return only active subscriptions or every subscription on record.

    :param value: If omitted defaults to "active". Must be one of ["active", "all"].
    :type value: str
    """

    allowed_values = {
        "active",
        "all",
    }
    ACTIVE: ClassVar["SampleLogGenerationSubscriptionsStatusFilter"]
    ALL: ClassVar["SampleLogGenerationSubscriptionsStatusFilter"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SampleLogGenerationSubscriptionsStatusFilter.ACTIVE = SampleLogGenerationSubscriptionsStatusFilter("active")
SampleLogGenerationSubscriptionsStatusFilter.ALL = SampleLogGenerationSubscriptionsStatusFilter("all")
