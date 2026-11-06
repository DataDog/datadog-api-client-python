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
    from datadog_api_client.v2.model.rum_recovery_session_status import RumRecoverySessionStatus


class RumArchiveSessionRecoveryStatus(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_recovery_session_status import RumRecoverySessionStatus

        return {
            "recovered_at": (datetime,),
            "request_id": (str,),
            "status": (RumRecoverySessionStatus,),
        }

    attribute_map = {
        "recovered_at": "recovered_at",
        "request_id": "request_id",
        "status": "status",
    }

    def __init__(
        self_,
        status: RumRecoverySessionStatus,
        recovered_at: Union[datetime, UnsetType] = unset,
        request_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Session recovery state. A missing recovery record can be represented as null. Optional request_id and recovered_at are omitted when unavailable.

        :param recovered_at: Recovery timestamp, when available.
        :type recovered_at: datetime, optional

        :param request_id: Associated recovery request ID.
        :type request_id: str, optional

        :param status: Session availability or recovery state. ``RECOVERED`` indicates that the session is ready to query.
        :type status: RumRecoverySessionStatus
        """
        if recovered_at is not unset:
            kwargs["recovered_at"] = recovered_at
        if request_id is not unset:
            kwargs["request_id"] = request_id
        super().__init__(kwargs)

        self_.status = status
