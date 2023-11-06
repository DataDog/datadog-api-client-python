# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class ServiceDefinitionV2SlackType(StringEnum):
    """
    Contact type.

    :param value: If omitted defaults to "slack". Must be one of ["slack"].
    :type value: str
    """

    allowed_values = {
        "slack",
    }
    SLACK: ClassVar["ServiceDefinitionV2SlackType"]


ServiceDefinitionV2SlackType.SLACK = ServiceDefinitionV2SlackType("slack")
