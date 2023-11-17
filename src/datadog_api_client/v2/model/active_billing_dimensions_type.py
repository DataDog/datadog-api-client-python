# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ActiveBillingDimensionsType(ModelSimple):
    """
    Type of active billing dimensions data.

    :param value: If omitted defaults to "billing_dimensions". Must be one of ["billing_dimensions"].
    :type value: str
    """

    allowed_values = {
        "billing_dimensions",
    }
    BILLING_DIMENSIONS: ClassVar["ActiveBillingDimensionsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ActiveBillingDimensionsType.BILLING_DIMENSIONS = ActiveBillingDimensionsType("billing_dimensions")
