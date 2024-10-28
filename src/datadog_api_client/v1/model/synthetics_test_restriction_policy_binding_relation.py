# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsTestRestrictionPolicyBindingRelation(ModelSimple):
    """
    The type of relation for the binding.

    :param value: Must be one of ["editor", "viewer"].
    :type value: str
    """

    allowed_values = {
        "editor",
        "viewer",
    }
    EDITOR: ClassVar["SyntheticsTestRestrictionPolicyBindingRelation"]
    VIEWER: ClassVar["SyntheticsTestRestrictionPolicyBindingRelation"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsTestRestrictionPolicyBindingRelation.EDITOR = SyntheticsTestRestrictionPolicyBindingRelation("editor")
SyntheticsTestRestrictionPolicyBindingRelation.VIEWER = SyntheticsTestRestrictionPolicyBindingRelation("viewer")
