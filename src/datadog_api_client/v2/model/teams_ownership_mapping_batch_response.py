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
    from datadog_api_client.v2.model.teams_ownership_mapping_batch_result import TeamsOwnershipMappingBatchResult
    from datadog_api_client.v2.model.teams_ownership_mapping_batch_error import TeamsOwnershipMappingBatchError


class TeamsOwnershipMappingBatchResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.teams_ownership_mapping_batch_result import TeamsOwnershipMappingBatchResult
        from datadog_api_client.v2.model.teams_ownership_mapping_batch_error import TeamsOwnershipMappingBatchError

        return {
            "atomic_results": ([TeamsOwnershipMappingBatchResult],),
            "errors": ([TeamsOwnershipMappingBatchError],),
        }

    attribute_map = {
        "atomic_results": "atomic:results",
        "errors": "errors",
    }

    def __init__(
        self_,
        atomic_results: Union[List[TeamsOwnershipMappingBatchResult], UnsetType] = unset,
        errors: Union[List[TeamsOwnershipMappingBatchError], UnsetType] = unset,
        **kwargs,
    ):
        """
        The response body for the bulk create and remove operation. On success, ``atomic:results``
        contains one entry per operation. Add results appear before remove results and may not match
        request order. Correlate add results by their ``type`` and ``id`` rather than by array position.
        On failure, no operations were applied and ``errors`` describes what went wrong.

        :param atomic_results: The result of each operation.
            Add operations are processed first, then remove operations, so results may not appear
            in the same order as the request. Present only on success.
        :type atomic_results: [TeamsOwnershipMappingBatchResult], optional

        :param errors: The validation or processing errors encountered. Present only when the request could not be completed.
        :type errors: [TeamsOwnershipMappingBatchError], optional
        """
        if atomic_results is not unset:
            kwargs["atomic_results"] = atomic_results
        if errors is not unset:
            kwargs["errors"] = errors
        super().__init__(kwargs)
