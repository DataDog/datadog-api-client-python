# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TestOptimizationFlakyTestsManagementPoliciesDisabledStatus(ModelSimple):
    """
    Test status that the disable policy applies to.
        Must be either `active` or `quarantined`.

    :param value: Must be one of ["active", "quarantined"].
    :type value: str
    """

    allowed_values = {
        "active",
        "quarantined",
    }
    ACTIVE: ClassVar["TestOptimizationFlakyTestsManagementPoliciesDisabledStatus"]
    QUARANTINED: ClassVar["TestOptimizationFlakyTestsManagementPoliciesDisabledStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TestOptimizationFlakyTestsManagementPoliciesDisabledStatus.ACTIVE = (
    TestOptimizationFlakyTestsManagementPoliciesDisabledStatus("active")
)
TestOptimizationFlakyTestsManagementPoliciesDisabledStatus.QUARANTINED = (
    TestOptimizationFlakyTestsManagementPoliciesDisabledStatus("quarantined")
)
