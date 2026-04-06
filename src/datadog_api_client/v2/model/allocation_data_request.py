# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.upsert_allocation_request import UpsertAllocationRequest
    from datadog_api_client.v2.model.allocation_data_type import AllocationDataType


class AllocationDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.upsert_allocation_request import UpsertAllocationRequest
        from datadog_api_client.v2.model.allocation_data_type import AllocationDataType

        return {
            "attributes": (UpsertAllocationRequest,),
            "type": (AllocationDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: UpsertAllocationRequest, type: AllocationDataType, **kwargs):
        """
        Data wrapper for allocation request payloads.

        :param attributes: Request to create or update a targeting rule (allocation) for a feature flag environment.
        :type attributes: UpsertAllocationRequest

        :param type: The resource type.
        :type type: AllocationDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
