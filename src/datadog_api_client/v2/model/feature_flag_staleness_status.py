# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FeatureFlagStalenessStatus(ModelSimple):
    """
    The computed staleness status of a feature flag.

    :param value: Must be one of ["ACTIVE", "STALE", "PERMANENT"].
    :type value: str
    """

    allowed_values = {
        "ACTIVE",
        "STALE",
        "PERMANENT",
    }
    ACTIVE: ClassVar["FeatureFlagStalenessStatus"]
    STALE: ClassVar["FeatureFlagStalenessStatus"]
    PERMANENT: ClassVar["FeatureFlagStalenessStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FeatureFlagStalenessStatus.ACTIVE = FeatureFlagStalenessStatus("ACTIVE")
FeatureFlagStalenessStatus.STALE = FeatureFlagStalenessStatus("STALE")
FeatureFlagStalenessStatus.PERMANENT = FeatureFlagStalenessStatus("PERMANENT")
