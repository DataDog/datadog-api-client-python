# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ScalarColumnTypeNumber(ModelSimple):
    """
    The type of column present for numbers.

    :param value: If omitted defaults to "number". Must be one of ["number"].
    :type value: str
    """

    allowed_values = {
        "number",
    }
    NUMBER: ClassVar["ScalarColumnTypeNumber"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ScalarColumnTypeNumber.NUMBER = ScalarColumnTypeNumber("number")
