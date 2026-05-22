# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SampleLogGenerationSubscriptionStatus(ModelSimple):
    """
    The status of the subscription.

    :param value: Must be one of ["subscribed", "renewed", "unsubscribed", "no_active_subscription", "not_available", "active", "expired"].
    :type value: str
    """

    allowed_values = {
        "subscribed",
        "renewed",
        "unsubscribed",
        "no_active_subscription",
        "not_available",
        "active",
        "expired",
    }
    SUBSCRIBED: ClassVar["SampleLogGenerationSubscriptionStatus"]
    RENEWED: ClassVar["SampleLogGenerationSubscriptionStatus"]
    UNSUBSCRIBED: ClassVar["SampleLogGenerationSubscriptionStatus"]
    NO_ACTIVE_SUBSCRIPTION: ClassVar["SampleLogGenerationSubscriptionStatus"]
    NOT_AVAILABLE: ClassVar["SampleLogGenerationSubscriptionStatus"]
    ACTIVE: ClassVar["SampleLogGenerationSubscriptionStatus"]
    EXPIRED: ClassVar["SampleLogGenerationSubscriptionStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SampleLogGenerationSubscriptionStatus.SUBSCRIBED = SampleLogGenerationSubscriptionStatus("subscribed")
SampleLogGenerationSubscriptionStatus.RENEWED = SampleLogGenerationSubscriptionStatus("renewed")
SampleLogGenerationSubscriptionStatus.UNSUBSCRIBED = SampleLogGenerationSubscriptionStatus("unsubscribed")
SampleLogGenerationSubscriptionStatus.NO_ACTIVE_SUBSCRIPTION = SampleLogGenerationSubscriptionStatus(
    "no_active_subscription"
)
SampleLogGenerationSubscriptionStatus.NOT_AVAILABLE = SampleLogGenerationSubscriptionStatus("not_available")
SampleLogGenerationSubscriptionStatus.ACTIVE = SampleLogGenerationSubscriptionStatus("active")
SampleLogGenerationSubscriptionStatus.EXPIRED = SampleLogGenerationSubscriptionStatus("expired")
