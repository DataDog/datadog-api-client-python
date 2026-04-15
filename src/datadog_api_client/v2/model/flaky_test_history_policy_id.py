# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FlakyTestHistoryPolicyId(ModelSimple):
    """
    The policy that triggered this status change.

    :param value: Must be one of ["ftm_policy.manual", "ftm_policy.fixed", "ftm_policy.disable.failure_rate", "ftm_policy.disable.branch_flake", "ftm_policy.disable.days_active", "ftm_policy.quarantine.failure_rate", "ftm_policy.quarantine.branch_flake", "ftm_policy.quarantine.days_active", "unknown"].
    :type value: str
    """

    allowed_values = {
        "ftm_policy.manual",
        "ftm_policy.fixed",
        "ftm_policy.disable.failure_rate",
        "ftm_policy.disable.branch_flake",
        "ftm_policy.disable.days_active",
        "ftm_policy.quarantine.failure_rate",
        "ftm_policy.quarantine.branch_flake",
        "ftm_policy.quarantine.days_active",
        "unknown",
    }
    MANUAL: ClassVar["FlakyTestHistoryPolicyId"]
    FIXED: ClassVar["FlakyTestHistoryPolicyId"]
    DISABLE_FAILURE_RATE: ClassVar["FlakyTestHistoryPolicyId"]
    DISABLE_BRANCH_FLAKE: ClassVar["FlakyTestHistoryPolicyId"]
    DISABLE_DAYS_ACTIVE: ClassVar["FlakyTestHistoryPolicyId"]
    QUARANTINE_FAILURE_RATE: ClassVar["FlakyTestHistoryPolicyId"]
    QUARANTINE_BRANCH_FLAKE: ClassVar["FlakyTestHistoryPolicyId"]
    QUARANTINE_DAYS_ACTIVE: ClassVar["FlakyTestHistoryPolicyId"]
    UNKNOWN: ClassVar["FlakyTestHistoryPolicyId"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FlakyTestHistoryPolicyId.MANUAL = FlakyTestHistoryPolicyId("ftm_policy.manual")
FlakyTestHistoryPolicyId.FIXED = FlakyTestHistoryPolicyId("ftm_policy.fixed")
FlakyTestHistoryPolicyId.DISABLE_FAILURE_RATE = FlakyTestHistoryPolicyId("ftm_policy.disable.failure_rate")
FlakyTestHistoryPolicyId.DISABLE_BRANCH_FLAKE = FlakyTestHistoryPolicyId("ftm_policy.disable.branch_flake")
FlakyTestHistoryPolicyId.DISABLE_DAYS_ACTIVE = FlakyTestHistoryPolicyId("ftm_policy.disable.days_active")
FlakyTestHistoryPolicyId.QUARANTINE_FAILURE_RATE = FlakyTestHistoryPolicyId("ftm_policy.quarantine.failure_rate")
FlakyTestHistoryPolicyId.QUARANTINE_BRANCH_FLAKE = FlakyTestHistoryPolicyId("ftm_policy.quarantine.branch_flake")
FlakyTestHistoryPolicyId.QUARANTINE_DAYS_ACTIVE = FlakyTestHistoryPolicyId("ftm_policy.quarantine.days_active")
FlakyTestHistoryPolicyId.UNKNOWN = FlakyTestHistoryPolicyId("unknown")
