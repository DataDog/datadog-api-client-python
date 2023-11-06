# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class ServiceDefinitionV2Dot2Version(StringEnum):
    """
    Schema version being used.

    :param value: If omitted defaults to "v2.2". Must be one of ["v2.2"].
    :type value: str
    """

    allowed_values = {
        "v2.2",
    }
    V2_2: ClassVar["ServiceDefinitionV2Dot2Version"]


ServiceDefinitionV2Dot2Version.V2_2 = ServiceDefinitionV2Dot2Version("v2.2")
