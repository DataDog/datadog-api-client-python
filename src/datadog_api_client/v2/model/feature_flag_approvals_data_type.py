# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FeatureFlagApprovalsDataType(ModelSimple):
    """
    The resource type for feature flag approval settings.

    :param value: If omitted defaults to "feature-flag-approvals". Must be one of ["feature-flag-approvals"].
    :type value: str
    """

    allowed_values = {
        "feature-flag-approvals",
    }
    FEATURE_FLAG_APPROVALS: ClassVar["FeatureFlagApprovalsDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FeatureFlagApprovalsDataType.FEATURE_FLAG_APPROVALS = FeatureFlagApprovalsDataType("feature-flag-approvals")
