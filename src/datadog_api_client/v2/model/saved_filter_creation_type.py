# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SavedFilterCreationType(ModelSimple):
    """
    How the saved filter was authored. RULES indicates rule-based authoring and LIST indicates list import. Both types return targeting rules and conditions.

    :param value: Must be one of ["RULES", "LIST"].
    :type value: str
    """

    allowed_values = {
        "RULES",
        "LIST",
    }
    RULES: ClassVar["SavedFilterCreationType"]
    LIST: ClassVar["SavedFilterCreationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SavedFilterCreationType.RULES = SavedFilterCreationType("RULES")
SavedFilterCreationType.LIST = SavedFilterCreationType("LIST")
