# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FeatureFlagStalenessStatusOverride(ModelSimple):
    """
    An explicit staleness status override. Omitted when no override is set.

    :param value: Must be one of ["STALE", "PERMANENT"].
    :type value: str
    """

    allowed_values = {
        "STALE",
        "PERMANENT",
    }
    STALE: ClassVar["FeatureFlagStalenessStatusOverride"]
    PERMANENT: ClassVar["FeatureFlagStalenessStatusOverride"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FeatureFlagStalenessStatusOverride.STALE = FeatureFlagStalenessStatusOverride("STALE")
FeatureFlagStalenessStatusOverride.PERMANENT = FeatureFlagStalenessStatusOverride("PERMANENT")
