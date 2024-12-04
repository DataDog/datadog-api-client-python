# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.external_user_group_patch_request_operations_items import (
        ExternalUserGroupPatchRequestOperationsItems,
    )


class ExternalUserGroupPatchRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.external_user_group_patch_request_operations_items import (
            ExternalUserGroupPatchRequestOperationsItems,
        )

        return {
            "operations": ([ExternalUserGroupPatchRequestOperationsItems],),
            "schemas": ([str],),
        }

    attribute_map = {
        "operations": "Operations",
        "schemas": "schemas",
    }

    def __init__(
        self_,
        operations: Union[List[ExternalUserGroupPatchRequestOperationsItems], UnsetType] = unset,
        schemas: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Request object for patching a SCIM group.

        :param operations: A list of update operations to be performed on a SCIM group.
        :type operations: [ExternalUserGroupPatchRequestOperationsItems], optional

        :param schemas: Input JSON Schemas
        :type schemas: [str], optional
        """
        if operations is not unset:
            kwargs["operations"] = operations
        if schemas is not unset:
            kwargs["schemas"] = schemas
        super().__init__(kwargs)
