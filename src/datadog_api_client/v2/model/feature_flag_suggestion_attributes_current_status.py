# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FeatureFlagSuggestionAttributesCurrentStatus(ModelSimple):
    """
    The legacy review status. Use `lifecycle_status` to distinguish approval from application.

    :param value: Must be one of ["pending", "approved", "rejected"].
    :type value: str
    """

    allowed_values = {
        "pending",
        "approved",
        "rejected",
    }
    PENDING: ClassVar["FeatureFlagSuggestionAttributesCurrentStatus"]
    APPROVED: ClassVar["FeatureFlagSuggestionAttributesCurrentStatus"]
    REJECTED: ClassVar["FeatureFlagSuggestionAttributesCurrentStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FeatureFlagSuggestionAttributesCurrentStatus.PENDING = FeatureFlagSuggestionAttributesCurrentStatus("pending")
FeatureFlagSuggestionAttributesCurrentStatus.APPROVED = FeatureFlagSuggestionAttributesCurrentStatus("approved")
FeatureFlagSuggestionAttributesCurrentStatus.REJECTED = FeatureFlagSuggestionAttributesCurrentStatus("rejected")
