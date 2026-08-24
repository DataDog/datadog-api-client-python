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
    from datadog_api_client.v2.model.teams_ownership_mapping_batch_result_data import (
        TeamsOwnershipMappingBatchResultData,
    )


class TeamsOwnershipMappingBatchResult(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.teams_ownership_mapping_batch_result_data import (
            TeamsOwnershipMappingBatchResultData,
        )

        return {
            "data": (TeamsOwnershipMappingBatchResultData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[TeamsOwnershipMappingBatchResultData, UnsetType] = unset, **kwargs):
        """
        The result of a single operation.
        Add operations are processed first, then remove operations, so results may not appear
        in the same order as the request. Empty for ``remove`` operations.

        :param data: The mapping created by an ``add`` operation.
        :type data: TeamsOwnershipMappingBatchResultData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
