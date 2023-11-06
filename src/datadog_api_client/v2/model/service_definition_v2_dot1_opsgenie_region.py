# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class ServiceDefinitionV2Dot1OpsgenieRegion(StringEnum):
    """
    Opsgenie instance region.

    :param value: Must be one of ["US", "EU"].
    :type value: str
    """

    allowed_values = {
        "US",
        "EU",
    }
    US: ClassVar["ServiceDefinitionV2Dot1OpsgenieRegion"]
    EU: ClassVar["ServiceDefinitionV2Dot1OpsgenieRegion"]


ServiceDefinitionV2Dot1OpsgenieRegion.US = ServiceDefinitionV2Dot1OpsgenieRegion("US")
ServiceDefinitionV2Dot1OpsgenieRegion.EU = ServiceDefinitionV2Dot1OpsgenieRegion("EU")
