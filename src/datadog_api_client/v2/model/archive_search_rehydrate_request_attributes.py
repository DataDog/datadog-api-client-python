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
    from datadog_api_client.v2.model.archive_search_rehydrate_request_rehydration import (
        ArchiveSearchRehydrateRequestRehydration,
    )


class ArchiveSearchRehydrateRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.archive_search_rehydrate_request_rehydration import (
            ArchiveSearchRehydrateRequestRehydration,
        )

        return {
            "rehydration": (ArchiveSearchRehydrateRequestRehydration,),
        }

    attribute_map = {
        "rehydration": "rehydration",
    }

    def __init__(self_, rehydration: ArchiveSearchRehydrateRequestRehydration, **kwargs):
        """
        Attributes accepted when rehydrating an Archive Search.

        :param rehydration: Rehydration settings to apply.
        :type rehydration: ArchiveSearchRehydrateRequestRehydration
        """
        super().__init__(kwargs)

        self_.rehydration = rehydration
