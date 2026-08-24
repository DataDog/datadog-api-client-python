# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TeamsOwnershipMappingBatchOperationOp(ModelSimple):
    """
    Whether this operation adds a new mapping or removes an existing one.

    :param value: Must be one of ["add", "remove"].
    :type value: str
    """

    allowed_values = {
        "add",
        "remove",
    }
    ADD: ClassVar["TeamsOwnershipMappingBatchOperationOp"]
    REMOVE: ClassVar["TeamsOwnershipMappingBatchOperationOp"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TeamsOwnershipMappingBatchOperationOp.ADD = TeamsOwnershipMappingBatchOperationOp("add")
TeamsOwnershipMappingBatchOperationOp.REMOVE = TeamsOwnershipMappingBatchOperationOp("remove")
