# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.rum_recovery_sessions_request_type import RUMRecoverySessionsRequestType
    from datadog_api_client.v2.model.rum_recovery_session_input import RUMRecoverySessionInput


class RUMRecoverySessionsCreateAttributes(ModelNormal):
    validations = {
        "sessions": {
            "max_items": 100,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_recovery_sessions_request_type import RUMRecoverySessionsRequestType
        from datadog_api_client.v2.model.rum_recovery_session_input import RUMRecoverySessionInput

        return {
            "request_type": (RUMRecoverySessionsRequestType,),
            "sessions": ([RUMRecoverySessionInput],),
        }

    attribute_map = {
        "request_type": "request_type",
        "sessions": "sessions",
    }

    def __init__(
        self_,
        sessions: List[RUMRecoverySessionInput],
        request_type: Union[RUMRecoverySessionsRequestType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Recover 1 to 100 explicit archived sessions. Session IDs must be unique within the request.

        :param request_type: Targeted recovery. Omitted request_type defaults to sessions.
        :type request_type: RUMRecoverySessionsRequestType, optional

        :param sessions: Sessions to recover.
        :type sessions: [RUMRecoverySessionInput]
        """
        if request_type is not unset:
            kwargs["request_type"] = request_type
        super().__init__(kwargs)

        self_.sessions = sessions
