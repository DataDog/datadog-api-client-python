# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityEntityRiskScoreType(ModelSimple):
    """
    Resource type

    :param value: If omitted defaults to "security_entity_risk_score". Must be one of ["security_entity_risk_score"].
    :type value: str
    """

    allowed_values = {
        "security_entity_risk_score",
    }
    SECURITY_ENTITY_RISK_SCORE: ClassVar["SecurityEntityRiskScoreType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityEntityRiskScoreType.SECURITY_ENTITY_RISK_SCORE = SecurityEntityRiskScoreType("security_entity_risk_score")
