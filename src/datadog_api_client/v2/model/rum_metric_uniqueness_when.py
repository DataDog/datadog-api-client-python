# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumMetricUniquenessWhen(ModelSimple):
    """
    When to count updatable events. `match` when the event is first seen, or `end` when the event is complete.

    :param value: Must be one of ["match", "end"].
    :type value: str
    """

    allowed_values = {
        "match",
        "end",
    }
    WHEN_MATCH: ClassVar["RumMetricUniquenessWhen"]
    WHEN_END: ClassVar["RumMetricUniquenessWhen"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumMetricUniquenessWhen.WHEN_MATCH = RumMetricUniquenessWhen("match")
RumMetricUniquenessWhen.WHEN_END = RumMetricUniquenessWhen("end")
