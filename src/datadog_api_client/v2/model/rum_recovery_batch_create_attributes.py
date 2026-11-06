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
    from datadog_api_client.v2.model.rum_recovery_batch_request_type import RumRecoveryBatchRequestType


class RumRecoveryBatchCreateAttributes(ModelNormal):
    validations = {
        "estimated_count": {
            "inclusive_minimum": 0,
        },
        "_from": {
            "inclusive_minimum": 1,
        },
        "to": {
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_recovery_batch_request_type import RumRecoveryBatchRequestType

        return {
            "estimated_count": (int,),
            "_from": (int,),
            "query": (str,),
            "request_type": (RumRecoveryBatchRequestType,),
            "to": (int,),
        }

    attribute_map = {
        "estimated_count": "estimated_count",
        "_from": "from",
        "query": "query",
        "request_type": "request_type",
        "to": "to",
    }

    def __init__(
        self_,
        _from: int,
        query: str,
        request_type: RumRecoveryBatchRequestType,
        to: int,
        estimated_count: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Recover sessions selected by a query. The range cannot exceed 180 days; from cannot be more than 4 years ago and to cannot be more than 1 hour in the future. Session availability depends on the configured archive retention.

        :param estimated_count: Optional client estimate. Creation validates and stores a fresh server estimate instead of this value.
        :type estimated_count: int, optional

        :param _from: Start of the range in Unix milliseconds. Must be positive and earlier than to.
        :type _from: int

        :param query: RUM search query. Not blank, at most 4096 bytes for batch creation and count.
        :type query: str

        :param request_type: Query-based batch recovery.
        :type request_type: RumRecoveryBatchRequestType

        :param to: End of the range in Unix milliseconds.
        :type to: int
        """
        if estimated_count is not unset:
            kwargs["estimated_count"] = estimated_count
        super().__init__(kwargs)

        self_._from = _from
        self_.query = query
        self_.request_type = request_type
        self_.to = to
