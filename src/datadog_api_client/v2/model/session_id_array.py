# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.session_id_data import SessionIdData


class SessionIdArray(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.session_id_data import SessionIdData

        return {
            "data": ([SessionIdData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[SessionIdData], **kwargs):
        """
        A collection of session identifiers used for bulk add or remove operations on a playlist.

        :param data: Array of session identifier data objects.
        :type data: [SessionIdData]
        """
        super().__init__(kwargs)

        self_.data = data
