# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsBanditPolicyHistoryV2DTODataType(ModelSimple):
    """
    Bandit policy resource type.

    :param value: If omitted defaults to "bandit-policies". Must be one of ["bandit-policies"].
    :type value: str
    """

    allowed_values = {
        "bandit-policies",
    }
    BANDIT_POLICIES: ClassVar["ExperimentsBanditPolicyHistoryV2DTODataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsBanditPolicyHistoryV2DTODataType.BANDIT_POLICIES = ExperimentsBanditPolicyHistoryV2DTODataType(
    "bandit-policies"
)
