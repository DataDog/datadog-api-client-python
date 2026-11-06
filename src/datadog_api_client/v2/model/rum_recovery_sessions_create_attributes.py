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
    from datadog_api_client.v2.model.rum_recovery_sessions_request_type import RumRecoverySessionsRequestType
    from datadog_api_client.v2.model.rum_recovery_session_input import RumRecoverySessionInput


class RumRecoverySessionsCreateAttributes(ModelNormal):
    validations = {
        "sessions": {
            "max_items": 100,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_recovery_sessions_request_type import RumRecoverySessionsRequestType
        from datadog_api_client.v2.model.rum_recovery_session_input import RumRecoverySessionInput

        return {
            "request_type": (RumRecoverySessionsRequestType,),
            "sessions": ([RumRecoverySessionInput],),
        }

    attribute_map = {
        "request_type": "request_type",
        "sessions": "sessions",
    }

    def __init__(
        self_,
        sessions: List[RumRecoverySessionInput],
        request_type: Union[RumRecoverySessionsRequestType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Recover 1 to 100 explicit archived sessions. Session IDs must be unique within the request.

        :param request_type: Targeted recovery. Omitted request_type defaults to sessions.
        :type request_type: RumRecoverySessionsRequestType, optional

        :param sessions: Sessions to recover.
        :type sessions: [RumRecoverySessionInput]
        """
        if request_type is not unset:
            kwargs["request_type"] = request_type
        super().__init__(kwargs)

        self_.sessions = sessions
