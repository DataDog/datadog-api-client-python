# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FeatureFlagDistributionChannel(ModelSimple):
    """
    The distribution channel for the feature flag.

    :param value: Must be one of ["ALL", "CLIENT", "SERVER"].
    :type value: str
    """

    allowed_values = {
        "ALL",
        "CLIENT",
        "SERVER",
    }
    ALL: ClassVar["FeatureFlagDistributionChannel"]
    CLIENT: ClassVar["FeatureFlagDistributionChannel"]
    SERVER: ClassVar["FeatureFlagDistributionChannel"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FeatureFlagDistributionChannel.ALL = FeatureFlagDistributionChannel("ALL")
FeatureFlagDistributionChannel.CLIENT = FeatureFlagDistributionChannel("CLIENT")
FeatureFlagDistributionChannel.SERVER = FeatureFlagDistributionChannel("SERVER")
