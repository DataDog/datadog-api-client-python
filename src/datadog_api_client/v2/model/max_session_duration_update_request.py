# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.max_session_duration_update_request_data import MaxSessionDurationUpdateRequestData


class MaxSessionDurationUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.max_session_duration_update_request_data import (
            MaxSessionDurationUpdateRequestData,
        )

        return {
            "data": (MaxSessionDurationUpdateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: MaxSessionDurationUpdateRequestData, **kwargs):
        """
        Request to update the maximum session duration.

        :param data: Data wrapper for maximum session duration update.
        :type data: MaxSessionDurationUpdateRequestData
        """
        super().__init__(kwargs)

        self_.data = data
