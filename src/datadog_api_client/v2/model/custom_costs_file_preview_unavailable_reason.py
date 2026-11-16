# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CustomCostsFilePreviewUnavailableReason(ModelSimple):
    """
    Reason the content of the Custom Costs file is not returned. Only set when `content` is omitted.

    :param value: If omitted defaults to "CHARGE_PERIOD_OUTSIDE_RETENTION_WINDOW". Must be one of ["CHARGE_PERIOD_OUTSIDE_RETENTION_WINDOW"].
    :type value: str
    """

    allowed_values = {
        "CHARGE_PERIOD_OUTSIDE_RETENTION_WINDOW",
    }
    CHARGE_PERIOD_OUTSIDE_RETENTION_WINDOW: ClassVar["CustomCostsFilePreviewUnavailableReason"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CustomCostsFilePreviewUnavailableReason.CHARGE_PERIOD_OUTSIDE_RETENTION_WINDOW = (
    CustomCostsFilePreviewUnavailableReason("CHARGE_PERIOD_OUTSIDE_RETENTION_WINDOW")
)
