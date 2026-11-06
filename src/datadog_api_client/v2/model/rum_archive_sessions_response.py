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
    from datadog_api_client.v2.model.rum_archive_session import RumArchiveSession
    from datadog_api_client.v2.model.rum_archive_sessions_meta import RumArchiveSessionsMeta


class RumArchiveSessionsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_archive_session import RumArchiveSession
        from datadog_api_client.v2.model.rum_archive_sessions_meta import RumArchiveSessionsMeta

        return {
            "data": ([RumArchiveSession],),
            "meta": (RumArchiveSessionsMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self_, data: List[RumArchiveSession], meta: RumArchiveSessionsMeta, **kwargs):
        """
        JSON:API document.

        :param data: Archived sessions.
        :type data: [RumArchiveSession]

        :param meta: Search metadata.
        :type meta: RumArchiveSessionsMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
