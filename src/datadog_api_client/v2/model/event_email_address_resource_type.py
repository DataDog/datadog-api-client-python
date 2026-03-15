# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class EventEmailAddressResourceType(ModelSimple):
    """
    The type of the resource. Must be `event_emails`.

    :param value: If omitted defaults to "event_emails". Must be one of ["event_emails"].
    :type value: str
    """

    allowed_values = {
        "event_emails",
    }
    EVENT_EMAILS: ClassVar["EventEmailAddressResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EventEmailAddressResourceType.EVENT_EMAILS = EventEmailAddressResourceType("event_emails")
