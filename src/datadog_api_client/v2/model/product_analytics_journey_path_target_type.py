# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsJourneyPathTargetType(ModelSimple):
    """
    The discriminator identifying a target that references a range of steps.

    :param value: If omitted defaults to "path". Must be one of ["path"].
    :type value: str
    """

    allowed_values = {
        "path",
    }
    PATH: ClassVar["ProductAnalyticsJourneyPathTargetType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsJourneyPathTargetType.PATH = ProductAnalyticsJourneyPathTargetType("path")
