# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsLaunchListScope(ModelSimple):
    """
    Scope of a launch list. `liftoffs` leaves out launches in the `plan` phase.

    :param value: If omitted defaults to "liftoffs". Must be one of ["liftoffs"].
    :type value: str
    """

    allowed_values = {
        "liftoffs",
    }
    LIFTOFFS: ClassVar["ProductAnalyticsLaunchListScope"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsLaunchListScope.LIFTOFFS = ProductAnalyticsLaunchListScope("liftoffs")
