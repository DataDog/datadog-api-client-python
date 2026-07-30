# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RUMOperationStrongLinkUpdateStatus(ModelSimple):
    """
    The status of a RUM operation strong link. Can only be set to `CONFIRMED` or `REJECTED`.

    :param value: Must be one of ["CONFIRMED", "REJECTED"].
    :type value: str
    """

    allowed_values = {
        "CONFIRMED",
        "REJECTED",
    }
    CONFIRMED: ClassVar["RUMOperationStrongLinkUpdateStatus"]
    REJECTED: ClassVar["RUMOperationStrongLinkUpdateStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RUMOperationStrongLinkUpdateStatus.CONFIRMED = RUMOperationStrongLinkUpdateStatus("CONFIRMED")
RUMOperationStrongLinkUpdateStatus.REJECTED = RUMOperationStrongLinkUpdateStatus("REJECTED")
