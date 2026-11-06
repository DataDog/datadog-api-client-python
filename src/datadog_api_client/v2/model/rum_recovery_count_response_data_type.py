# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumRecoveryCountResponseDataType(ModelSimple):
    """
    JSON:API resource type.

    :param value: If omitted defaults to "rum_recovery_count". Must be one of ["rum_recovery_count"].
    :type value: str
    """

    allowed_values = {
        "rum_recovery_count",
    }
    RUM_RECOVERY_COUNT: ClassVar["RumRecoveryCountResponseDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumRecoveryCountResponseDataType.RUM_RECOVERY_COUNT = RumRecoveryCountResponseDataType("rum_recovery_count")
