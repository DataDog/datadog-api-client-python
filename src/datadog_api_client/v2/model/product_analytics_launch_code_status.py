# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsLaunchCodeStatus(ModelSimple):
    """
    Whether the inspected code sends the event, or attaches the property to the event.

    :param value: Must be one of ["found", "not_found"].
    :type value: str
    """

    allowed_values = {
        "found",
        "not_found",
    }
    FOUND: ClassVar["ProductAnalyticsLaunchCodeStatus"]
    NOT_FOUND: ClassVar["ProductAnalyticsLaunchCodeStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsLaunchCodeStatus.FOUND = ProductAnalyticsLaunchCodeStatus("found")
ProductAnalyticsLaunchCodeStatus.NOT_FOUND = ProductAnalyticsLaunchCodeStatus("not_found")
