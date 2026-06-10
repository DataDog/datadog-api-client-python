# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OwnershipHistoryType(ModelSimple):
    """
    The type of the ownership history resource. The value should always be `ownership_history`.

    :param value: If omitted defaults to "ownership_history". Must be one of ["ownership_history"].
    :type value: str
    """

    allowed_values = {
        "ownership_history",
    }
    OWNERSHIP_HISTORY: ClassVar["OwnershipHistoryType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OwnershipHistoryType.OWNERSHIP_HISTORY = OwnershipHistoryType("ownership_history")
