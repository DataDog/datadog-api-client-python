# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OrgGroupPolicySuggestionStatus(ModelSimple):
    """
    The status of the policy suggestion.

    :param value: Must be one of ["pending", "accepted", "dismissed"].
    :type value: str
    """

    allowed_values = {
        "pending",
        "accepted",
        "dismissed",
    }
    PENDING: ClassVar["OrgGroupPolicySuggestionStatus"]
    ACCEPTED: ClassVar["OrgGroupPolicySuggestionStatus"]
    DISMISSED: ClassVar["OrgGroupPolicySuggestionStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OrgGroupPolicySuggestionStatus.PENDING = OrgGroupPolicySuggestionStatus("pending")
OrgGroupPolicySuggestionStatus.ACCEPTED = OrgGroupPolicySuggestionStatus("accepted")
OrgGroupPolicySuggestionStatus.DISMISSED = OrgGroupPolicySuggestionStatus("dismissed")
