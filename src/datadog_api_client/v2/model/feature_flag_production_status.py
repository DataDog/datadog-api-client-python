# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FeatureFlagProductionStatus(ModelSimple):
    """
    The status of a feature flag across production environments.

    :param value: Must be one of ["ENABLED", "DISABLED", "OVERRIDDEN"].
    :type value: str
    """

    allowed_values = {
        "ENABLED",
        "DISABLED",
        "OVERRIDDEN",
    }
    ENABLED: ClassVar["FeatureFlagProductionStatus"]
    DISABLED: ClassVar["FeatureFlagProductionStatus"]
    OVERRIDDEN: ClassVar["FeatureFlagProductionStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FeatureFlagProductionStatus.ENABLED = FeatureFlagProductionStatus("ENABLED")
FeatureFlagProductionStatus.DISABLED = FeatureFlagProductionStatus("DISABLED")
FeatureFlagProductionStatus.OVERRIDDEN = FeatureFlagProductionStatus("OVERRIDDEN")
