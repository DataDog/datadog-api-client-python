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
    from datadog_api_client.v2.model.archive_search_rehydration_tier import ArchiveSearchRehydrationTier


class ArchiveSearchRehydrateRequestRehydration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.archive_search_rehydration_tier import ArchiveSearchRehydrationTier

        return {
            "retention_days": (int,),
            "tier": (ArchiveSearchRehydrationTier,),
        }

    attribute_map = {
        "retention_days": "retention_days",
        "tier": "tier",
    }

    def __init__(self_, retention_days: int, tier: ArchiveSearchRehydrationTier, **kwargs):
        """
        Rehydration settings to apply.

        :param retention_days: Number of days the rehydrated logs are retained for.
        :type retention_days: int

        :param tier: Storage tier the matched logs are rehydrated into.
        :type tier: ArchiveSearchRehydrationTier
        """
        super().__init__(kwargs)

        self_.retention_days = retention_days
        self_.tier = tier
