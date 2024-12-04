# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.external_user_group_patch_request_operations_items_op import (
        ExternalUserGroupPatchRequestOperationsItemsOp,
    )


class ExternalUserGroupPatchRequestOperationsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.external_user_group_patch_request_operations_items_op import (
            ExternalUserGroupPatchRequestOperationsItemsOp,
        )

        return {
            "op": (ExternalUserGroupPatchRequestOperationsItemsOp,),
            "path": (str,),
            "value": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
        }

    attribute_map = {
        "op": "op",
        "path": "path",
        "value": "value",
    }

    def __init__(
        self_,
        op: Union[ExternalUserGroupPatchRequestOperationsItemsOp, UnsetType] = unset,
        path: Union[str, UnsetType] = unset,
        value: Union[Any, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of an individual patch operation in a patch request.

        :param op: The operation to be performed.
        :type op: ExternalUserGroupPatchRequestOperationsItemsOp, optional

        :param path: An attribute path describing the target of the operation.
        :type path: str, optional

        :param value: JSON element containing the target values required to apply the patch operation.
        :type value: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional
        """
        if op is not unset:
            kwargs["op"] = op
        if path is not unset:
            kwargs["path"] = path
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)
