# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SampleLogGenerationBulkSubscriptionRequestType(ModelSimple):
    """
    The type of the resource. The value should always be `bulk_subscription_requests`.

    :param value: If omitted defaults to "bulk_subscription_requests". Must be one of ["bulk_subscription_requests"].
    :type value: str
    """

    allowed_values = {
        "bulk_subscription_requests",
    }
    BULK_SUBSCRIPTION_REQUESTS: ClassVar["SampleLogGenerationBulkSubscriptionRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SampleLogGenerationBulkSubscriptionRequestType.BULK_SUBSCRIPTION_REQUESTS = (
    SampleLogGenerationBulkSubscriptionRequestType("bulk_subscription_requests")
)
