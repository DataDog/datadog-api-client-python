# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RolloutStrategy(ModelSimple):
    """
    The progression strategy used by a progressive rollout.

    :param value: Must be one of ["UNIFORM_INTERVALS", "NO_ROLLOUT"].
    :type value: str
    """

    allowed_values = {
        "UNIFORM_INTERVALS",
        "NO_ROLLOUT",
    }
    UNIFORM_INTERVALS: ClassVar["RolloutStrategy"]
    NO_ROLLOUT: ClassVar["RolloutStrategy"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RolloutStrategy.UNIFORM_INTERVALS = RolloutStrategy("UNIFORM_INTERVALS")
RolloutStrategy.NO_ROLLOUT = RolloutStrategy("NO_ROLLOUT")
