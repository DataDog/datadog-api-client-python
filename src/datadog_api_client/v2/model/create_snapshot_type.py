# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CreateSnapshotType(ModelSimple):
    """
    The type identifier for snapshot creation resources.

    :param value: If omitted defaults to "create_snapshot". Must be one of ["create_snapshot"].
    :type value: str
    """

    allowed_values = {
        "create_snapshot",
    }
    CREATE_SNAPSHOT: ClassVar["CreateSnapshotType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CreateSnapshotType.CREATE_SNAPSHOT = CreateSnapshotType("create_snapshot")
