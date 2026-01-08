# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class JsonPatchOperationOp(ModelSimple):
    """
    The operation to perform.

    :param value: Must be one of ["add", "remove", "replace", "move", "copy", "test"].
    :type value: str
    """

    allowed_values = {
        "add",
        "remove",
        "replace",
        "move",
        "copy",
        "test",
    }
    ADD: ClassVar["JsonPatchOperationOp"]
    REMOVE: ClassVar["JsonPatchOperationOp"]
    REPLACE: ClassVar["JsonPatchOperationOp"]
    MOVE: ClassVar["JsonPatchOperationOp"]
    COPY: ClassVar["JsonPatchOperationOp"]
    TEST: ClassVar["JsonPatchOperationOp"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


JsonPatchOperationOp.ADD = JsonPatchOperationOp("add")
JsonPatchOperationOp.REMOVE = JsonPatchOperationOp("remove")
JsonPatchOperationOp.REPLACE = JsonPatchOperationOp("replace")
JsonPatchOperationOp.MOVE = JsonPatchOperationOp("move")
JsonPatchOperationOp.COPY = JsonPatchOperationOp("copy")
JsonPatchOperationOp.TEST = JsonPatchOperationOp("test")
