# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RetentionReturnCondition(ModelSimple):
    """
    Condition for counting user return.

    :param value: Must be one of ["conversion_on", "conversion_on_or_after"].
    :type value: str
    """

    allowed_values = {
        "conversion_on",
        "conversion_on_or_after",
    }
    CONVERSION_ON: ClassVar["RetentionReturnCondition"]
    CONVERSION_ON_OR_AFTER: ClassVar["RetentionReturnCondition"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RetentionReturnCondition.CONVERSION_ON = RetentionReturnCondition("conversion_on")
RetentionReturnCondition.CONVERSION_ON_OR_AFTER = RetentionReturnCondition("conversion_on_or_after")
