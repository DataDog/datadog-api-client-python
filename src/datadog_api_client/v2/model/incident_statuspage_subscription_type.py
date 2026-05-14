# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentStatuspageSubscriptionType(ModelSimple):
    """
    Statuspage email subscription resource type.

    :param value: If omitted defaults to "statuspage_email_subscription". Must be one of ["statuspage_email_subscription"].
    :type value: str
    """

    allowed_values = {
        "statuspage_email_subscription",
    }
    STATUSPAGE_EMAIL_SUBSCRIPTION: ClassVar["IncidentStatuspageSubscriptionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentStatuspageSubscriptionType.STATUSPAGE_EMAIL_SUBSCRIPTION = IncidentStatuspageSubscriptionType(
    "statuspage_email_subscription"
)
