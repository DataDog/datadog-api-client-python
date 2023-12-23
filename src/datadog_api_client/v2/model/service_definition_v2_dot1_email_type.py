# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class ServiceDefinitionV2Dot1EmailType(StringEnum):
    """
    Contact type.

    :param value: If omitted defaults to "email". Must be one of ["email"].
    :type value: str
    """

    allowed_values = {
        "email",
    }
    EMAIL: ClassVar["ServiceDefinitionV2Dot1EmailType"]


ServiceDefinitionV2Dot1EmailType.EMAIL = ServiceDefinitionV2Dot1EmailType("email")
