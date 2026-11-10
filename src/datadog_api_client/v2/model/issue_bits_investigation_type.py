# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IssueBitsInvestigationType(ModelSimple):
    """
    Type of the object.

    :param value: If omitted defaults to "bits_investigation". Must be one of ["bits_investigation"].
    :type value: str
    """

    allowed_values = {
        "bits_investigation",
    }
    BITS_INVESTIGATION: ClassVar["IssueBitsInvestigationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IssueBitsInvestigationType.BITS_INVESTIGATION = IssueBitsInvestigationType("bits_investigation")
