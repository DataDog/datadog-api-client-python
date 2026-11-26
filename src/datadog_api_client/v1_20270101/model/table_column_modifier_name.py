# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TableColumnModifierName(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["fill", "as_count", "as_rate", "weighted", "rollup"].
    :type value: str
    """

    allowed_values = {
        "fill",
        "as_count",
        "as_rate",
        "weighted",
        "rollup",
    }
    FILL: ClassVar["TableColumnModifierName"]
    AS_COUNT: ClassVar["TableColumnModifierName"]
    AS_RATE: ClassVar["TableColumnModifierName"]
    WEIGHTED: ClassVar["TableColumnModifierName"]
    ROLLUP: ClassVar["TableColumnModifierName"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TableColumnModifierName.FILL = TableColumnModifierName("fill")
TableColumnModifierName.AS_COUNT = TableColumnModifierName("as_count")
TableColumnModifierName.AS_RATE = TableColumnModifierName("as_rate")
TableColumnModifierName.WEIGHTED = TableColumnModifierName("weighted")
TableColumnModifierName.ROLLUP = TableColumnModifierName("rollup")
