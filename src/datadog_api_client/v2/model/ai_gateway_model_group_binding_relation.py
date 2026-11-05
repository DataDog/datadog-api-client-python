# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayModelGroupBindingRelation(ModelSimple):
    """
    Access relation granted on a model group.

    :param value: Must be one of ["viewer", "runner", "editor"].
    :type value: str
    """

    allowed_values = {
        "viewer",
        "runner",
        "editor",
    }
    VIEWER: ClassVar["AiGatewayModelGroupBindingRelation"]
    RUNNER: ClassVar["AiGatewayModelGroupBindingRelation"]
    EDITOR: ClassVar["AiGatewayModelGroupBindingRelation"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayModelGroupBindingRelation.VIEWER = AiGatewayModelGroupBindingRelation("viewer")
AiGatewayModelGroupBindingRelation.RUNNER = AiGatewayModelGroupBindingRelation("runner")
AiGatewayModelGroupBindingRelation.EDITOR = AiGatewayModelGroupBindingRelation("editor")
