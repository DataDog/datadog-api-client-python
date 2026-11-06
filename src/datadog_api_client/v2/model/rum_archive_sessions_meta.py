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
    from datadog_api_client.v2.model.rum_archive_sessions_page import RumArchiveSessionsPage


class RumArchiveSessionsMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_archive_sessions_page import RumArchiveSessionsPage

        return {
            "page": (RumArchiveSessionsPage,),
        }

    attribute_map = {
        "page": "page",
    }

    def __init__(self_, page: RumArchiveSessionsPage, **kwargs):
        """
        Search metadata.

        :param page: Search pagination.
        :type page: RumArchiveSessionsPage
        """
        super().__init__(kwargs)

        self_.page = page
