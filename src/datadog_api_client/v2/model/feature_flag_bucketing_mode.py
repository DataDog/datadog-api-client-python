# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FeatureFlagBucketingMode(ModelSimple):
    """
    How subjects are assigned to variants. `DATADOG` is the native scheme. `EPPO` reproduces the assignments that Eppo made for a flag migrated from Eppo, so its subjects keep their variants. Set when the flag is created and never changed.

    :param value: Must be one of ["DATADOG", "EPPO"].
    :type value: str
    """

    allowed_values = {
        "DATADOG",
        "EPPO",
    }
    DATADOG: ClassVar["FeatureFlagBucketingMode"]
    EPPO: ClassVar["FeatureFlagBucketingMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FeatureFlagBucketingMode.DATADOG = FeatureFlagBucketingMode("DATADOG")
FeatureFlagBucketingMode.EPPO = FeatureFlagBucketingMode("EPPO")
