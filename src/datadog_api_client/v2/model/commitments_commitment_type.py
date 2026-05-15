# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CommitmentsCommitmentType(ModelSimple):
    """
    Type of commitment. ri for Reserved Instances, sp for Savings Plans.

    :param value: Must be one of ["ri", "sp"].
    :type value: str
    """

    allowed_values = {
        "ri",
        "sp",
    }
    RESERVED_INSTANCES: ClassVar["CommitmentsCommitmentType"]
    SAVINGS_PLANS: ClassVar["CommitmentsCommitmentType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CommitmentsCommitmentType.RESERVED_INSTANCES = CommitmentsCommitmentType("ri")
CommitmentsCommitmentType.SAVINGS_PLANS = CommitmentsCommitmentType("sp")
