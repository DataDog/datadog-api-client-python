# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FeatureFlagChangeEventSuggestionStatus(ModelSimple):
    """
    The review status of the change request.

    :param value: Must be one of ["pending", "approved", "rejected"].
    :type value: str
    """

    allowed_values = {
        "pending",
        "approved",
        "rejected",
    }
    PENDING: ClassVar["FeatureFlagChangeEventSuggestionStatus"]
    APPROVED: ClassVar["FeatureFlagChangeEventSuggestionStatus"]
    REJECTED: ClassVar["FeatureFlagChangeEventSuggestionStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FeatureFlagChangeEventSuggestionStatus.PENDING = FeatureFlagChangeEventSuggestionStatus("pending")
FeatureFlagChangeEventSuggestionStatus.APPROVED = FeatureFlagChangeEventSuggestionStatus("approved")
FeatureFlagChangeEventSuggestionStatus.REJECTED = FeatureFlagChangeEventSuggestionStatus("rejected")
