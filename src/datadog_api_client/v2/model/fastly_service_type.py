# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class FastlyServiceType(StringEnum):
    """
    The JSON:API type for this API. Should always be `fastly-services`.

    :param value: If omitted defaults to "fastly-services". Must be one of ["fastly-services"].
    :type value: str
    """

    allowed_values = {
        "fastly-services",
    }
    FASTLY_SERVICES: ClassVar["FastlyServiceType"]


FastlyServiceType.FASTLY_SERVICES = FastlyServiceType("fastly-services")
