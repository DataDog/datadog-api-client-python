# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.rum_archive_session_recovery_status import RumArchiveSessionRecoveryStatus


class RumArchiveSessionAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_archive_session_recovery_status import RumArchiveSessionRecoveryStatus

        return {
            "account_id": (str, none_type),
            "anonymous_id": (str, none_type),
            "application_id": (UUID,),
            "country": (str, none_type),
            "recovery_status": (RumArchiveSessionRecoveryStatus,),
            "service": (str,),
            "session_id": (str,),
            "timestamp": (int,),
            "user_id": (str, none_type),
            "version": (str, none_type),
        }

    attribute_map = {
        "account_id": "account_id",
        "anonymous_id": "anonymous_id",
        "application_id": "application_id",
        "country": "country",
        "recovery_status": "recovery_status",
        "service": "service",
        "session_id": "session_id",
        "timestamp": "timestamp",
        "user_id": "user_id",
        "version": "version",
    }

    def __init__(
        self_,
        account_id: Union[str, none_type],
        anonymous_id: Union[str, none_type],
        application_id: UUID,
        country: Union[str, none_type],
        recovery_status: Union[RumArchiveSessionRecoveryStatus, none_type],
        service: str,
        session_id: str,
        timestamp: int,
        user_id: Union[str, none_type],
        version: Union[str, none_type],
        **kwargs,
    ):
        """
        Archived session metadata.

        :param account_id: Session account id, or null when unavailable.
        :type account_id: str, none_type

        :param anonymous_id: Session anonymous id, or null when unavailable.
        :type anonymous_id: str, none_type

        :param application_id: Application UUID.
        :type application_id: UUID

        :param country: Session country, or null when unavailable.
        :type country: str, none_type

        :param recovery_status: Session recovery state. A missing recovery record can be represented as null. Optional request_id and recovered_at are omitted when unavailable.
        :type recovery_status: RumArchiveSessionRecoveryStatus, none_type

        :param service: Service name.
        :type service: str

        :param session_id: Session identifier.
        :type session_id: str

        :param timestamp: Session timestamp in Unix milliseconds.
        :type timestamp: int

        :param user_id: Session user id, or null when unavailable.
        :type user_id: str, none_type

        :param version: Session version, or null when unavailable.
        :type version: str, none_type
        """
        super().__init__(kwargs)

        self_.account_id = account_id
        self_.anonymous_id = anonymous_id
        self_.application_id = application_id
        self_.country = country
        self_.recovery_status = recovery_status
        self_.service = service
        self_.session_id = session_id
        self_.timestamp = timestamp
        self_.user_id = user_id
        self_.version = version
