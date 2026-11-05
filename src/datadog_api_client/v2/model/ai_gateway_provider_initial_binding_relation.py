# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayProviderInitialBindingRelation(ModelSimple):
    """
    Provider access relation. Editor also grants View.

    :param value: Must be one of ["viewer", "editor"].
    :type value: str
    """

    allowed_values = {
        "viewer",
        "editor",
    }
    VIEWER: ClassVar["AiGatewayProviderInitialBindingRelation"]
    EDITOR: ClassVar["AiGatewayProviderInitialBindingRelation"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayProviderInitialBindingRelation.VIEWER = AiGatewayProviderInitialBindingRelation("viewer")
AiGatewayProviderInitialBindingRelation.EDITOR = AiGatewayProviderInitialBindingRelation("editor")
