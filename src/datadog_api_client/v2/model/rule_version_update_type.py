# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RuleVersionUpdateType(ModelSimple):
    """
    The type of change.

    :param value: Must be one of ["create", "update", "delete"].
    :type value: str
    """

    allowed_values = {
        "create",
        "update",
        "delete",
    }
    CREATE: ClassVar["RuleVersionUpdateType"]
    UPDATE: ClassVar["RuleVersionUpdateType"]
    DELETE: ClassVar["RuleVersionUpdateType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RuleVersionUpdateType.CREATE = RuleVersionUpdateType("create")
RuleVersionUpdateType.UPDATE = RuleVersionUpdateType("update")
RuleVersionUpdateType.DELETE = RuleVersionUpdateType("delete")
