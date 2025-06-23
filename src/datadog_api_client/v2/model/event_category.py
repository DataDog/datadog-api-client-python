# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class EventCategory(ModelSimple):
    """
    Event category to identify the type of event. Only the value `change` is supported. Support for other categories are coming. please reach out to datadog support if you're interested.

    :param value: If omitted defaults to "change". Must be one of ["change"].
    :type value: str
    """

    allowed_values = {
        "change",
    }
    CHANGE: ClassVar["EventCategory"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EventCategory.CHANGE = EventCategory("change")
