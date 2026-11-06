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


class RumRecoveryCreateResponseAttributes(ModelNormal):
    validations = {
        "estimated_count": {
            "inclusive_minimum": 0,
        },
        "failed_sessions": {
            "inclusive_minimum": 0,
        },
        "processed_sessions": {
            "inclusive_minimum": 0,
        },
        "total_sessions": {
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
            "failed_sessions": (int,),
            "processed_sessions": (int,),
            "status": (RumRecoveryRequestStatus,),
            "total_sessions": (int,),
        }

    attribute_map = {
        "created_at": "created_at",
        "discovery_status": "discovery_status",
        "estimated_count": "estimated_count",
        "failed_sessions": "failed_sessions",
        "processed_sessions": "processed_sessions",
        "status": "status",
        "total_sessions": "total_sessions",
    }

    def __init__(
        self_,
        created_at: datetime,
        failed_sessions: int,
        processed_sessions: int,
        status: RumRecoveryRequestStatus,
        discovery_status: Union[RumRecoveryDiscoveryStatus, UnsetType] = unset,
        estimated_count: Union[int, UnsetType] = unset,
        total_sessions: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Accepted recovery request.

        :param created_at: Creation time.
        :type created_at: datetime

        :param discovery_status: Batch discovery state. QUEUED indicates that the request is waiting for processing capacity.
        :type discovery_status: RumRecoveryDiscoveryStatus, optional

        :param estimated_count: Batch estimate stored at creation, when present. New batches use a fresh server estimate; older batches may contain a client-supplied estimate.
        :type estimated_count: int, optional

        :param failed_sessions: Failed session count.
        :type failed_sessions: int

        :param processed_sessions: Processed session count.
        :type processed_sessions: int

        :param status: Recovery request state.
        :type status: RumRecoveryRequestStatus

        :param total_sessions: Total targeted sessions. Omitted while a batch total is unknown.
        :type total_sessions: int, optional
        """
        if discovery_status is not unset:
            kwargs["discovery_status"] = discovery_status
        if estimated_count is not unset:
            kwargs["estimated_count"] = estimated_count
        if total_sessions is not unset:
            kwargs["total_sessions"] = total_sessions
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.failed_sessions = failed_sessions
        self_.processed_sessions = processed_sessions
        self_.status = status
