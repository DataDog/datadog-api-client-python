# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CreateFeatureFlagStalenessStatus(ModelSimple):
    """
    The staleness status for the feature flag at creation.

    :param value: Must be one of ["ACTIVE", "PERMANENT"].
    :type value: str
    """

    allowed_values = {
        "ACTIVE",
        "PERMANENT",
    }
    ACTIVE: ClassVar["CreateFeatureFlagStalenessStatus"]
    PERMANENT: ClassVar["CreateFeatureFlagStalenessStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CreateFeatureFlagStalenessStatus.ACTIVE = CreateFeatureFlagStalenessStatus("ACTIVE")
CreateFeatureFlagStalenessStatus.PERMANENT = CreateFeatureFlagStalenessStatus("PERMANENT")
