# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class ServiceMapWidgetDefinitionType(StringEnum):
    """
    Type of the service map widget.

    :param value: If omitted defaults to "servicemap". Must be one of ["servicemap"].
    :type value: str
    """

    allowed_values = {
        "servicemap",
    }
    SERVICEMAP: ClassVar["ServiceMapWidgetDefinitionType"]


ServiceMapWidgetDefinitionType.SERVICEMAP = ServiceMapWidgetDefinitionType("servicemap")
