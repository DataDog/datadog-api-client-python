# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.rum_recovery_discovery_status import RumRecoveryDiscoveryStatus
    from datadog_api_client.v2.model.rum_recovery_request_status import RumRecoveryRequestStatus


class RumRecoveryBatchListAttributes(ModelNormal):
    validations = {
        "estimated_count": {
            "inclusive_minimum": 0,
        },
        "_from": {
            "inclusive_minimum": 1,
        },
        "sessions_discovered": {
            "inclusive_minimum": 0,
        },
        "sessions_failed": {
            "inclusive_minimum": 0,
        },
        "sessions_processed": {
            "inclusive_minimum": 0,
        },
        "slices_completed": {
            "inclusive_minimum": 0,
        },
        "slices_failed": {
            "inclusive_minimum": 0,
        },
        "to": {
            "inclusive_minimum": 1,
        },
        "total_slices": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_recovery_discovery_status import RumRecoveryDiscoveryStatus
        from datadog_api_client.v2.model.rum_recovery_request_status import RumRecoveryRequestStatus

        return {
            "created_at": (datetime,),
            "discovery_status": (RumRecoveryDiscoveryStatus,),
            "estimated_count": (int,),
            "_from": (int,),
            "query": (str,),
            "sessions_discovered": (int,),
            "sessions_failed": (int,),
            "sessions_processed": (int,),
            "slices_completed": (int,),
            "slices_failed": (int,),
            "status": (RumRecoveryRequestStatus,),
            "to": (int,),
            "total_slices": (int,),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "created_at": "created_at",
        "discovery_status": "discovery_status",
        "estimated_count": "estimated_count",
        "_from": "from",
        "query": "query",
        "sessions_discovered": "sessions_discovered",
        "sessions_failed": "sessions_failed",
        "sessions_processed": "sessions_processed",
        "slices_completed": "slices_completed",
        "slices_failed": "slices_failed",
        "status": "status",
        "to": "to",
        "total_slices": "total_slices",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        created_at: datetime,
        discovery_status: RumRecoveryDiscoveryStatus,
        _from: int,
        query: str,
        sessions_discovered: int,
        sessions_failed: int,
        sessions_processed: int,
        slices_completed: int,
        slices_failed: int,
        status: RumRecoveryRequestStatus,
        to: int,
        total_slices: int,
        updated_at: datetime,
        estimated_count: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Batch recovery progress. Status updates can appear here before they appear in request details.

        :param created_at: Creation time.
        :type created_at: datetime

        :param discovery_status: Batch discovery state. QUEUED indicates that the request is waiting for processing capacity.
        :type discovery_status: RumRecoveryDiscoveryStatus

        :param estimated_count: Batch estimate stored at creation, when present. New batches use a fresh server estimate; older batches may contain a client-supplied estimate.
        :type estimated_count: int, optional

        :param _from: Start of the range in Unix milliseconds. Must be positive and earlier than to.
        :type _from: int

        :param query: RUM search query. Not blank, at most 4096 bytes for batch creation and count.
        :type query: str

        :param sessions_discovered: Discovered sessions.
        :type sessions_discovered: int

        :param sessions_failed: Failed sessions.
        :type sessions_failed: int

        :param sessions_processed: Processed sessions.
        :type sessions_processed: int

        :param slices_completed: Completed slices.
        :type slices_completed: int

        :param slices_failed: Failed slices.
        :type slices_failed: int

        :param status: Recovery request state.
        :type status: RumRecoveryRequestStatus

        :param to: End of the range in Unix milliseconds.
        :type to: int

        :param total_slices: Total discovery slices.
        :type total_slices: int

        :param updated_at: Last update time.
        :type updated_at: datetime
        """
        if estimated_count is not unset:
            kwargs["estimated_count"] = estimated_count
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.discovery_status = discovery_status
        self_._from = _from
        self_.query = query
        self_.sessions_discovered = sessions_discovered
        self_.sessions_failed = sessions_failed
        self_.sessions_processed = sessions_processed
        self_.slices_completed = slices_completed
        self_.slices_failed = slices_failed
        self_.status = status
        self_.to = to
        self_.total_slices = total_slices
        self_.updated_at = updated_at
