# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class UsageSortDirection(StringEnum):
    """
    The direction to sort by.

    :param value: If omitted defaults to "desc". Must be one of ["desc", "asc"].
    :type value: str
    """

    allowed_values = {
        "desc",
        "asc",
    }
    DESC: ClassVar["UsageSortDirection"]
    ASC: ClassVar["UsageSortDirection"]


UsageSortDirection.DESC = UsageSortDirection("desc")
UsageSortDirection.ASC = UsageSortDirection("asc")
