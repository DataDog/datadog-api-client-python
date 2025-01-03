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
    from datadog_api_client.v2.model.action_connection_data import ActionConnectionData


class CreateActionConnectionRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.action_connection_data import ActionConnectionData

        return {
            "data": (ActionConnectionData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ActionConnectionData, **kwargs):
        """
        Request used to create an action connection.

        :param data: Data related to the connection.
        :type data: ActionConnectionData
        """
        super().__init__(kwargs)

        self_.data = data
