# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SampleLogGenerationSubscriptionRequestType(ModelSimple):
    """
    The type of the resource. The value should always be `subscription_requests`.

    :param value: If omitted defaults to "subscription_requests". Must be one of ["subscription_requests"].
    :type value: str
    """

    allowed_values = {
        "subscription_requests",
    }
    SUBSCRIPTION_REQUESTS: ClassVar["SampleLogGenerationSubscriptionRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SampleLogGenerationSubscriptionRequestType.SUBSCRIPTION_REQUESTS = SampleLogGenerationSubscriptionRequestType(
    "subscription_requests"
)
