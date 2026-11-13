# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsBanditPolicyKind(ModelSimple):
    """
    WARMUP serves the arms equally. ADAPTIVE serves the initial split or a split from a refresh. FALLBACK serves one variant after the bandit ends.

    :param value: Must be one of ["WARMUP", "ADAPTIVE", "FALLBACK"].
    :type value: str
    """

    allowed_values = {
        "WARMUP",
        "ADAPTIVE",
        "FALLBACK",
    }
    WARMUP: ClassVar["ExperimentsBanditPolicyKind"]
    ADAPTIVE: ClassVar["ExperimentsBanditPolicyKind"]
    FALLBACK: ClassVar["ExperimentsBanditPolicyKind"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsBanditPolicyKind.WARMUP = ExperimentsBanditPolicyKind("WARMUP")
ExperimentsBanditPolicyKind.ADAPTIVE = ExperimentsBanditPolicyKind("ADAPTIVE")
ExperimentsBanditPolicyKind.FALLBACK = ExperimentsBanditPolicyKind("FALLBACK")
