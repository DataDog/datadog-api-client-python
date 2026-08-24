# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.teams_ownership_mapping_batch_operation_data import (
        TeamsOwnershipMappingBatchOperationData,
    )
    from datadog_api_client.v2.model.teams_ownership_mapping_batch_operation_op import (
        TeamsOwnershipMappingBatchOperationOp,
    )
    from datadog_api_client.v2.model.teams_ownership_mapping_batch_operation_ref import (
        TeamsOwnershipMappingBatchOperationRef,
    )


class TeamsOwnershipMappingBatchOperation(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.teams_ownership_mapping_batch_operation_data import (
            TeamsOwnershipMappingBatchOperationData,
        )
        from datadog_api_client.v2.model.teams_ownership_mapping_batch_operation_op import (
            TeamsOwnershipMappingBatchOperationOp,
        )
        from datadog_api_client.v2.model.teams_ownership_mapping_batch_operation_ref import (
            TeamsOwnershipMappingBatchOperationRef,
        )

        return {
            "data": (TeamsOwnershipMappingBatchOperationData,),
            "op": (TeamsOwnershipMappingBatchOperationOp,),
            "ref": (TeamsOwnershipMappingBatchOperationRef,),
        }

    attribute_map = {
        "data": "data",
        "op": "op",
        "ref": "ref",
    }

    def __init__(
        self_,
        op: TeamsOwnershipMappingBatchOperationOp,
        data: Union[TeamsOwnershipMappingBatchOperationData, UnsetType] = unset,
        ref: Union[TeamsOwnershipMappingBatchOperationRef, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single add or remove operation, applied atomically with every other operation in the request.

        :param data: The mapping to add. Required when ``op`` is ``add``.
        :type data: TeamsOwnershipMappingBatchOperationData, optional

        :param op: Whether this operation adds a new mapping or removes an existing one.
        :type op: TeamsOwnershipMappingBatchOperationOp

        :param ref: Identifies an existing mapping to remove. Required when ``op`` is ``remove``.
        :type ref: TeamsOwnershipMappingBatchOperationRef, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if ref is not unset:
            kwargs["ref"] = ref
        super().__init__(kwargs)

        self_.op = op
