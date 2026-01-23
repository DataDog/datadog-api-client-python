# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RevertCustomRuleRevisionDataType(ModelSimple):
    """
    Request type

    :param value: If omitted defaults to "revert_custom_rule_revision_request". Must be one of ["revert_custom_rule_revision_request"].
    :type value: str
    """

    allowed_values = {
        "revert_custom_rule_revision_request",
    }
    REVERT_CUSTOM_RULE_REVISION_REQUEST: ClassVar["RevertCustomRuleRevisionDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RevertCustomRuleRevisionDataType.REVERT_CUSTOM_RULE_REVISION_REQUEST = RevertCustomRuleRevisionDataType(
    "revert_custom_rule_revision_request"
)
