# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.rum_recovery_discovery_status import RumRecoveryDiscoveryStatus
    from datadog_api_client.v2.model.rum_recovery_batch_request_type import RumRecoveryBatchRequestType
    from datadog_api_client.v2.model.rum_recovered_session import RumRecoveredSession
    from datadog_api_client.v2.model.rum_recovery_request_status import RumRecoveryRequestStatus


class RumRecoveryRequestAttributes(ModelNormal):
    validations = {
        "estimated_count": {
            "inclusive_minimum": 0,
        },
        "failed_sessions": {
            "inclusive_minimum": 0,
        },
        "_from": {
            "inclusive_minimum": 1,
        },
        "processed_sessions": {
            "inclusive_minimum": 0,
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
        "total_sessions": {
            "inclusive_minimum": 0,
        },
        "total_slices": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_recovery_discovery_status import RumRecoveryDiscoveryStatus
        from datadog_api_client.v2.model.rum_recovery_batch_request_type import RumRecoveryBatchRequestType
        from datadog_api_client.v2.model.rum_recovered_session import RumRecoveredSession
        from datadog_api_client.v2.model.rum_recovery_request_status import RumRecoveryRequestStatus

        return {
            "created_at": (datetime,),
            "discovery_status": (RumRecoveryDiscoveryStatus,),
            "error_message": (str,),
            "estimated_count": (int,),
            "failed_sessions": (int,),
            "_from": (int,),
            "processed_sessions": (int,),
            "query": (str,),
            "request_type": (RumRecoveryBatchRequestType,),
            "sessions": ([RumRecoveredSession],),
            "sessions_discovered": (int,),
            "sessions_failed": (int,),
            "sessions_processed": (int,),
            "slices_completed": (int,),
            "slices_failed": (int,),
            "status": (RumRecoveryRequestStatus,),
            "to": (int,),
            "total_sessions": (int,),
            "total_slices": (int,),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "created_at": "created_at",
        "discovery_status": "discovery_status",
        "error_message": "error_message",
        "estimated_count": "estimated_count",
        "failed_sessions": "failed_sessions",
        "_from": "from",
        "processed_sessions": "processed_sessions",
        "query": "query",
        "request_type": "request_type",
        "sessions": "sessions",
        "sessions_discovered": "sessions_discovered",
        "sessions_failed": "sessions_failed",
        "sessions_processed": "sessions_processed",
        "slices_completed": "slices_completed",
        "slices_failed": "slices_failed",
        "status": "status",
        "to": "to",
        "total_sessions": "total_sessions",
        "total_slices": "total_slices",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        created_at: datetime,
        failed_sessions: int,
        processed_sessions: int,
        status: RumRecoveryRequestStatus,
        updated_at: datetime,
        discovery_status: Union[RumRecoveryDiscoveryStatus, UnsetType] = unset,
        error_message: Union[str, UnsetType] = unset,
        estimated_count: Union[int, UnsetType] = unset,
        _from: Union[int, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        request_type: Union[RumRecoveryBatchRequestType, UnsetType] = unset,
        sessions: Union[List[RumRecoveredSession], UnsetType] = unset,
        sessions_discovered: Union[int, UnsetType] = unset,
        sessions_failed: Union[int, UnsetType] = unset,
        sessions_processed: Union[int, UnsetType] = unset,
        slices_completed: Union[int, UnsetType] = unset,
        slices_failed: Union[int, UnsetType] = unset,
        to: Union[int, UnsetType] = unset,
        total_sessions: Union[int, UnsetType] = unset,
        total_slices: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Recovery progress. Batch-only attributes are omitted for targeted requests; request_type is also omitted for targeted requests.

        :param created_at: Creation time.
        :type created_at: datetime

        :param discovery_status: Batch discovery state. QUEUED indicates that the request is waiting for processing capacity.
        :type discovery_status: RumRecoveryDiscoveryStatus, optional

        :param error_message: Failure details, if present.
        :type error_message: str, optional

        :param estimated_count: Batch estimate stored at creation, when present. New batches use a fresh server estimate; older batches may contain a client-supplied estimate.
        :type estimated_count: int, optional

        :param failed_sessions: Failed session count.
        :type failed_sessions: int

        :param _from: Start of the range in Unix milliseconds. Must be positive and earlier than to.
        :type _from: int, optional

        :param processed_sessions: Processed session count.
        :type processed_sessions: int

        :param query: RUM search query. Not blank, at most 4096 bytes for batch creation and count.
        :type query: str, optional

        :param request_type: Query-based batch recovery.
        :type request_type: RumRecoveryBatchRequestType, optional

        :param sessions: Targeted session progress. Omitted when empty or not applicable.
        :type sessions: [RumRecoveredSession], optional

        :param sessions_discovered: Discovered sessions.
        :type sessions_discovered: int, optional

        :param sessions_failed: Failed sessions.
        :type sessions_failed: int, optional

        :param sessions_processed: Processed sessions.
        :type sessions_processed: int, optional

        :param slices_completed: Completed slices.
        :type slices_completed: int, optional

        :param slices_failed: Failed slices.
        :type slices_failed: int, optional

        :param status: Recovery request state.
        :type status: RumRecoveryRequestStatus

        :param to: End of the range in Unix milliseconds.
        :type to: int, optional

        :param total_sessions: Total targeted sessions. Omitted while a batch total is unknown.
        :type total_sessions: int, optional

        :param total_slices: Total discovery slices.
        :type total_slices: int, optional

        :param updated_at: Last update time.
        :type updated_at: datetime
        """
        if discovery_status is not unset:
            kwargs["discovery_status"] = discovery_status
        if error_message is not unset:
            kwargs["error_message"] = error_message
        if estimated_count is not unset:
            kwargs["estimated_count"] = estimated_count
        if _from is not unset:
            kwargs["_from"] = _from
        if query is not unset:
            kwargs["query"] = query
        if request_type is not unset:
            kwargs["request_type"] = request_type
        if sessions is not unset:
            kwargs["sessions"] = sessions
        if sessions_discovered is not unset:
            kwargs["sessions_discovered"] = sessions_discovered
        if sessions_failed is not unset:
            kwargs["sessions_failed"] = sessions_failed
        if sessions_processed is not unset:
            kwargs["sessions_processed"] = sessions_processed
        if slices_completed is not unset:
            kwargs["slices_completed"] = slices_completed
        if slices_failed is not unset:
            kwargs["slices_failed"] = slices_failed
        if to is not unset:
            kwargs["to"] = to
        if total_sessions is not unset:
            kwargs["total_sessions"] = total_sessions
        if total_slices is not unset:
            kwargs["total_slices"] = total_slices
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.failed_sessions = failed_sessions
        self_.processed_sessions = processed_sessions
        self_.status = status
        self_.updated_at = updated_at
