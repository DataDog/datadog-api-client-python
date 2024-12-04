# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExternalUserGroupPatchRequestOperationsItemsOp(ModelSimple):
    """
    The operation to be performed.

    :param value: Must be one of ["add", "replace", "remove"].
    :type value: str
    """

    allowed_values = {
        "add",
        "replace",
        "remove",
    }
    ADD: ClassVar["ExternalUserGroupPatchRequestOperationsItemsOp"]
    REPLACE: ClassVar["ExternalUserGroupPatchRequestOperationsItemsOp"]
    REMOVE: ClassVar["ExternalUserGroupPatchRequestOperationsItemsOp"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExternalUserGroupPatchRequestOperationsItemsOp.ADD = ExternalUserGroupPatchRequestOperationsItemsOp("add")
ExternalUserGroupPatchRequestOperationsItemsOp.REPLACE = ExternalUserGroupPatchRequestOperationsItemsOp("replace")
ExternalUserGroupPatchRequestOperationsItemsOp.REMOVE = ExternalUserGroupPatchRequestOperationsItemsOp("remove")
