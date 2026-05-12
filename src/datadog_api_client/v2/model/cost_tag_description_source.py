# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CostTagDescriptionSource(ModelSimple):
    """
    Origin of the description. `human` indicates the description was written by a user, `ai_generated` was produced by AI, and `datadog` is a default supplied by Datadog.

    :param value: Must be one of ["human", "ai_generated", "datadog"].
    :type value: str
    """

    allowed_values = {
        "human",
        "ai_generated",
        "datadog",
    }
    HUMAN: ClassVar["CostTagDescriptionSource"]
    AI_GENERATED: ClassVar["CostTagDescriptionSource"]
    DATADOG: ClassVar["CostTagDescriptionSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CostTagDescriptionSource.HUMAN = CostTagDescriptionSource("human")
CostTagDescriptionSource.AI_GENERATED = CostTagDescriptionSource("ai_generated")
CostTagDescriptionSource.DATADOG = CostTagDescriptionSource("datadog")
