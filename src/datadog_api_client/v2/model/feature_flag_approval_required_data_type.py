# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FeatureFlagApprovalRequiredDataType(ModelSimple):
    """
    The resource type for an approval-required response.

    :param value: If omitted defaults to "approval-required". Must be one of ["approval-required"].
    :type value: str
    """

    allowed_values = {
        "approval-required",
    }
    APPROVAL_REQUIRED: ClassVar["FeatureFlagApprovalRequiredDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FeatureFlagApprovalRequiredDataType.APPROVAL_REQUIRED = FeatureFlagApprovalRequiredDataType("approval-required")
