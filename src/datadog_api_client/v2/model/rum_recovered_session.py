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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.rum_recovery_session_status import RumRecoverySessionStatus


class RumRecoveredSession(ModelNormal):
    validations = {
        "events_recovered": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_recovery_session_status import RumRecoverySessionStatus

        return {
            "application_id": (UUID,),
            "error_message": (str,),
            "events_recovered": (int,),
            "session_id": (UUID,),
            "status": (RumRecoverySessionStatus,),
        }

    attribute_map = {
        "application_id": "application_id",
        "error_message": "error_message",
        "events_recovered": "events_recovered",
        "session_id": "session_id",
        "status": "status",
    }

    def __init__(
        self_,
        application_id: UUID,
        events_recovered: int,
        session_id: UUID,
        status: RumRecoverySessionStatus,
        error_message: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Progress for one targeted session.

        :param application_id: Application UUID.
        :type application_id: UUID

        :param error_message: Failure details, if present.
        :type error_message: str, optional

        :param events_recovered: Recovered event count.
        :type events_recovered: int

        :param session_id: Session identifier.
        :type session_id: UUID

        :param status: Session availability or recovery state. ``RECOVERED`` indicates that the session is ready to query.
        :type status: RumRecoverySessionStatus
        """
        if error_message is not unset:
            kwargs["error_message"] = error_message
        super().__init__(kwargs)

        self_.application_id = application_id
        self_.events_recovered = events_recovered
        self_.session_id = session_id
        self_.status = status
