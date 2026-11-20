# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class QueryTableDatePattern(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["MMM dd yyyy", "MMM d", "MMM d, yyyy", "MM/dd/yyyy", "dd/MM/yyyy", "MMMM d, yyyy"].
    :type value: str
    """

    allowed_values = {
        "MMM dd yyyy",
        "MMM d",
        "MMM d, yyyy",
        "MM/dd/yyyy",
        "dd/MM/yyyy",
        "MMMM d, yyyy",
    }
    MMM_DD_YYYY: ClassVar["QueryTableDatePattern"]
    MMM_D: ClassVar["QueryTableDatePattern"]
    MMM_D__YYYY: ClassVar["QueryTableDatePattern"]
    MM_DD_YYYY: ClassVar["QueryTableDatePattern"]
    DD_MM_YYYY: ClassVar["QueryTableDatePattern"]
    MMMM_D__YYYY: ClassVar["QueryTableDatePattern"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


QueryTableDatePattern.MMM_DD_YYYY = QueryTableDatePattern("MMM dd yyyy")
QueryTableDatePattern.MMM_D = QueryTableDatePattern("MMM d")
QueryTableDatePattern.MMM_D__YYYY = QueryTableDatePattern("MMM d, yyyy")
QueryTableDatePattern.MM_DD_YYYY = QueryTableDatePattern("MM/dd/yyyy")
QueryTableDatePattern.DD_MM_YYYY = QueryTableDatePattern("dd/MM/yyyy")
QueryTableDatePattern.MMMM_D__YYYY = QueryTableDatePattern("MMMM d, yyyy")
