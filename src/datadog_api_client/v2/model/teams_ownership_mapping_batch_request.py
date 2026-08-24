# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.teams_ownership_mapping_batch_operation import TeamsOwnershipMappingBatchOperation


class TeamsOwnershipMappingBatchRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.teams_ownership_mapping_batch_operation import (
            TeamsOwnershipMappingBatchOperation,
        )

        return {
            "atomic_operations": ([TeamsOwnershipMappingBatchOperation],),
        }

    attribute_map = {
        "atomic_operations": "atomic:operations",
    }

    def __init__(self_, atomic_operations: List[TeamsOwnershipMappingBatchOperation], **kwargs):
        """
        The request body for bulk-creating and bulk-removing teams ownership mappings.

        :param atomic_operations: The list of add and remove operations to apply atomically.
        :type atomic_operations: [TeamsOwnershipMappingBatchOperation]
        """
        super().__init__(kwargs)

        self_.atomic_operations = atomic_operations
