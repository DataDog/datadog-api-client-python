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
    from datadog_api_client.v2.model.archive_search_rehydrate_request_data import ArchiveSearchRehydrateRequestData


class ArchiveSearchRehydrateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.archive_search_rehydrate_request_data import ArchiveSearchRehydrateRequestData

        return {
            "data": (ArchiveSearchRehydrateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ArchiveSearchRehydrateRequestData, **kwargs):
        """
        Request to rehydrate an Archive Search.

        :param data: Archive Search object to rehydrate.
        :type data: ArchiveSearchRehydrateRequestData
        """
        super().__init__(kwargs)

        self_.data = data
