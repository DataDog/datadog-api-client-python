# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FeatureFlagSuggestionAttributesLifecycleStatus(ModelSimple):
    """
    The lifecycle status of the suggestion.

    :param value: Must be one of ["pending", "approved", "applied", "rejected", "discarded"].
    :type value: str
    """

    allowed_values = {
        "pending",
        "approved",
        "applied",
        "rejected",
        "discarded",
    }
    PENDING: ClassVar["FeatureFlagSuggestionAttributesLifecycleStatus"]
    APPROVED: ClassVar["FeatureFlagSuggestionAttributesLifecycleStatus"]
    APPLIED: ClassVar["FeatureFlagSuggestionAttributesLifecycleStatus"]
    REJECTED: ClassVar["FeatureFlagSuggestionAttributesLifecycleStatus"]
    DISCARDED: ClassVar["FeatureFlagSuggestionAttributesLifecycleStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FeatureFlagSuggestionAttributesLifecycleStatus.PENDING = FeatureFlagSuggestionAttributesLifecycleStatus("pending")
FeatureFlagSuggestionAttributesLifecycleStatus.APPROVED = FeatureFlagSuggestionAttributesLifecycleStatus("approved")
FeatureFlagSuggestionAttributesLifecycleStatus.APPLIED = FeatureFlagSuggestionAttributesLifecycleStatus("applied")
FeatureFlagSuggestionAttributesLifecycleStatus.REJECTED = FeatureFlagSuggestionAttributesLifecycleStatus("rejected")
FeatureFlagSuggestionAttributesLifecycleStatus.DISCARDED = FeatureFlagSuggestionAttributesLifecycleStatus("discarded")
