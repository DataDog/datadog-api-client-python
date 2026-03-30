# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentUserDefinedFieldCategory(ModelSimple):
    """
    The section in which the field appears: "what_happened" or "why_it_happened". When null, the field appears in the Attributes section.

    :param value: Must be one of ["what_happened", "why_it_happened"].
    :type value: str
    """

    allowed_values = {
        "what_happened",
        "why_it_happened",
    }
    WHAT_HAPPENED: ClassVar["IncidentUserDefinedFieldCategory"]
    WHY_IT_HAPPENED: ClassVar["IncidentUserDefinedFieldCategory"]

    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentUserDefinedFieldCategory.WHAT_HAPPENED = IncidentUserDefinedFieldCategory("what_happened")
IncidentUserDefinedFieldCategory.WHY_IT_HAPPENED = IncidentUserDefinedFieldCategory("why_it_happened")
