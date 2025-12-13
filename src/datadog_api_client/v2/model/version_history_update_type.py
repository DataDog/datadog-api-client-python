# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class VersionHistoryUpdateType(ModelSimple):
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
    CREATE: ClassVar["VersionHistoryUpdateType"]
    UPDATE: ClassVar["VersionHistoryUpdateType"]
    DELETE: ClassVar["VersionHistoryUpdateType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


VersionHistoryUpdateType.CREATE = VersionHistoryUpdateType("create")
VersionHistoryUpdateType.UPDATE = VersionHistoryUpdateType("update")
VersionHistoryUpdateType.DELETE = VersionHistoryUpdateType("delete")
