# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class UpdateFeatureFlagStalenessStatus(ModelSimple):
    """
    The lifecycle to set. `ACTIVE` makes the flag temporary; `PERMANENT` excludes it from
        staleness detection. Either value clears any snooze; omit the field to keep the lifecycle.
        Do not copy the top-level `staleness_status` from a response into this field: that legacy
        response field is always `ACTIVE`.

    :param value: Must be one of ["ACTIVE", "PERMANENT"].
    :type value: str
    """

    allowed_values = {
        "ACTIVE",
        "PERMANENT",
    }
    ACTIVE: ClassVar["UpdateFeatureFlagStalenessStatus"]
    PERMANENT: ClassVar["UpdateFeatureFlagStalenessStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


UpdateFeatureFlagStalenessStatus.ACTIVE = UpdateFeatureFlagStalenessStatus("ACTIVE")
UpdateFeatureFlagStalenessStatus.PERMANENT = UpdateFeatureFlagStalenessStatus("PERMANENT")
