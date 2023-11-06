# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class DistributionWidgetDefinitionType(StringEnum):
    """
    Type of the distribution widget.

    :param value: If omitted defaults to "distribution". Must be one of ["distribution"].
    :type value: str
    """

    allowed_values = {
        "distribution",
    }
    DISTRIBUTION: ClassVar["DistributionWidgetDefinitionType"]


DistributionWidgetDefinitionType.DISTRIBUTION = DistributionWidgetDefinitionType("distribution")
