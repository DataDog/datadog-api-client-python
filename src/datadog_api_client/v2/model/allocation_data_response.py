# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.allocation import Allocation
    from datadog_api_client.v2.model.allocation_data_type import AllocationDataType


class AllocationDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.allocation import Allocation
        from datadog_api_client.v2.model.allocation_data_type import AllocationDataType

        return {
            "attributes": (Allocation,),
            "id": (UUID,),
            "type": (AllocationDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: Allocation, id: UUID, type: AllocationDataType, **kwargs):
        """
        Data wrapper for targeting rule allocation responses.

        :param attributes: Targeting rule (allocation) details for a feature flag environment.
        :type attributes: Allocation

        :param id: The unique identifier of the targeting rule allocation.
        :type id: UUID

        :param type: The resource type.
        :type type: AllocationDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
