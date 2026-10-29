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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.temporary_grant_request_grant_state import TemporaryGrantRequestGrantState
    from datadog_api_client.v2.model.temporary_grant_request_status import TemporaryGrantRequestStatus


class TemporaryGrantRequestAttributes(ModelNormal):
    validations = {
        "justification": {
            "max_length": 4096,
            "min_length": 1,
        },
        "total": {
            "inclusive_maximum": 9223372036854,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.temporary_grant_request_grant_state import TemporaryGrantRequestGrantState
        from datadog_api_client.v2.model.temporary_grant_request_status import TemporaryGrantRequestStatus

        return {
            "created_at": (datetime,),
            "decided_at": (datetime,),
            "decided_by_user_id": (UUID,),
            "entity_key": (str,),
            "expires_at": (datetime,),
            "grant_state": (TemporaryGrantRequestGrantState,),
            "justification": (str,),
            "quota_namespace": (str,),
            "requested_by_user_id": (UUID,),
            "status": (TemporaryGrantRequestStatus,),
            "total": (int,),
        }

    attribute_map = {
        "created_at": "created_at",
        "decided_at": "decided_at",
        "decided_by_user_id": "decided_by_user_id",
        "entity_key": "entity_key",
        "expires_at": "expires_at",
        "grant_state": "grant_state",
        "justification": "justification",
        "quota_namespace": "quota_namespace",
        "requested_by_user_id": "requested_by_user_id",
        "status": "status",
        "total": "total",
    }

    def __init__(
        self_,
        created_at: datetime,
        entity_key: str,
        expires_at: datetime,
        justification: str,
        quota_namespace: str,
        requested_by_user_id: UUID,
        status: TemporaryGrantRequestStatus,
        total: int,
        decided_at: Union[datetime, UnsetType] = unset,
        decided_by_user_id: Union[UUID, UnsetType] = unset,
        grant_state: Union[TemporaryGrantRequestGrantState, UnsetType] = unset,
        **kwargs,
    ):
        """
        Request history and the linked grant state. List and detail reads include grant_state for approved requests. Decision responses record the decision. Read the request for current grant state.

        :param created_at: When the request was submitted.
        :type created_at: datetime

        :param decided_at: When the decision or cancellation was recorded.
        :type decided_at: datetime, optional

        :param decided_by_user_id: UUID of the reviewer, or of the requester if the request was canceled.
        :type decided_by_user_id: UUID, optional

        :param entity_key: The requester identity resolved by the server.
        :type entity_key: str

        :param expires_at: Immutable exclusive expiry, normalized to UTC microsecond precision.
        :type expires_at: datetime

        :param grant_state: Current state of the grant associated with an approved request. Replaced means a newer grant superseded this grant. The newer grant might no longer be active. This field is absent for requests that weren't approved.
        :type grant_state: TemporaryGrantRequestGrantState, optional

        :param justification: Reason for requesting temporary credits. Trimmed and limited to 4096 UTF-8 bytes.
        :type justification: str

        :param quota_namespace: The quota namespace. Only AI credits are supported.
        :type quota_namespace: str

        :param requested_by_user_id: UUID of the authenticated requester.
        :type requested_by_user_id: UUID

        :param status: The durable request decision, independent of whether its grant is still active.
        :type status: TemporaryGrantRequestStatus

        :param total: Target monthly AI credit limit in positive whole credits, not additional credits. Fractional credits are not accepted.
        :type total: int
        """
        if decided_at is not unset:
            kwargs["decided_at"] = decided_at
        if decided_by_user_id is not unset:
            kwargs["decided_by_user_id"] = decided_by_user_id
        if grant_state is not unset:
            kwargs["grant_state"] = grant_state
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.entity_key = entity_key
        self_.expires_at = expires_at
        self_.justification = justification
        self_.quota_namespace = quota_namespace
        self_.requested_by_user_id = requested_by_user_id
        self_.status = status
        self_.total = total
