# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class CloudConfigurationRuleType(StringEnum):
    """
    The rule type.

    :param value: If omitted defaults to "cloud_configuration". Must be one of ["cloud_configuration"].
    :type value: str
    """

    allowed_values = {
        "cloud_configuration",
    }
    CLOUD_CONFIGURATION: ClassVar["CloudConfigurationRuleType"]


CloudConfigurationRuleType.CLOUD_CONFIGURATION = CloudConfigurationRuleType("cloud_configuration")
