# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayModelGroupType(ModelSimple):
    """
    AI Gateway model group resource type.

    :param value: If omitted defaults to "model-groups". Must be one of ["model-groups"].
    :type value: str
    """

    allowed_values = {
        "model-groups",
    }
    MODEL_GROUPS: ClassVar["AiGatewayModelGroupType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayModelGroupType.MODEL_GROUPS = AiGatewayModelGroupType("model-groups")
