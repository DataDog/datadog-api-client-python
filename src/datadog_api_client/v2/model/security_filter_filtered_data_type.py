# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class SecurityFilterFilteredDataType(StringEnum):
    """
    The filtered data type.

    :param value: If omitted defaults to "logs". Must be one of ["logs"].
    :type value: str
    """

    allowed_values = {
        "logs",
    }
    LOGS: ClassVar["SecurityFilterFilteredDataType"]


SecurityFilterFilteredDataType.LOGS = SecurityFilterFilteredDataType("logs")
