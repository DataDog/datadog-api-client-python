# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FeatureFlagChangeEventSuggestionLifecycleStatus(ModelSimple):
    """
    Where the change request is in its lifecycle.

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
    PENDING: ClassVar["FeatureFlagChangeEventSuggestionLifecycleStatus"]
    APPROVED: ClassVar["FeatureFlagChangeEventSuggestionLifecycleStatus"]
    APPLIED: ClassVar["FeatureFlagChangeEventSuggestionLifecycleStatus"]
    REJECTED: ClassVar["FeatureFlagChangeEventSuggestionLifecycleStatus"]
    DISCARDED: ClassVar["FeatureFlagChangeEventSuggestionLifecycleStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FeatureFlagChangeEventSuggestionLifecycleStatus.PENDING = FeatureFlagChangeEventSuggestionLifecycleStatus("pending")
FeatureFlagChangeEventSuggestionLifecycleStatus.APPROVED = FeatureFlagChangeEventSuggestionLifecycleStatus("approved")
FeatureFlagChangeEventSuggestionLifecycleStatus.APPLIED = FeatureFlagChangeEventSuggestionLifecycleStatus("applied")
FeatureFlagChangeEventSuggestionLifecycleStatus.REJECTED = FeatureFlagChangeEventSuggestionLifecycleStatus("rejected")
FeatureFlagChangeEventSuggestionLifecycleStatus.DISCARDED = FeatureFlagChangeEventSuggestionLifecycleStatus("discarded")
