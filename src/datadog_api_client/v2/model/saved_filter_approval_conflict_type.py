# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SavedFilterApprovalConflictType(ModelSimple):
    """
    The resource type for this saved filter update error.

    :param value: If omitted defaults to "update-approval-conflict". Must be one of ["update-approval-conflict"].
    :type value: str
    """

    allowed_values = {
        "update-approval-conflict",
    }
    UPDATE_APPROVAL_CONFLICT: ClassVar["SavedFilterApprovalConflictType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SavedFilterApprovalConflictType.UPDATE_APPROVAL_CONFLICT = SavedFilterApprovalConflictType("update-approval-conflict")
