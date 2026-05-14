# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentPagerdutyServiceType(ModelSimple):
    """
    PagerDuty service resource type.

    :param value: If omitted defaults to "pagerduty_service". Must be one of ["pagerduty_service"].
    :type value: str
    """

    allowed_values = {
        "pagerduty_service",
    }
    PAGERDUTY_SERVICE: ClassVar["IncidentPagerdutyServiceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentPagerdutyServiceType.PAGERDUTY_SERVICE = IncidentPagerdutyServiceType("pagerduty_service")
