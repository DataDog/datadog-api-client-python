# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class SecurityFilterType(StringEnum):
    """
    The type of the resource. The value should always be `security_filters`.

    :param value: If omitted defaults to "security_filters". Must be one of ["security_filters"].
    :type value: str
    """

    allowed_values = {
        "security_filters",
    }
    SECURITY_FILTERS: ClassVar["SecurityFilterType"]


SecurityFilterType.SECURITY_FILTERS = SecurityFilterType("security_filters")
