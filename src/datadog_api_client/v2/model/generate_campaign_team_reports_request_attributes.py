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
    from datadog_api_client.v2.model.entity_owner_destination import EntityOwnerDestination


class GenerateCampaignTeamReportsRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_owner_destination import EntityOwnerDestination

        return {
            "entity_owners": ([EntityOwnerDestination],),
        }

    attribute_map = {
        "entity_owners": "entity_owners",
    }

    def __init__(self_, entity_owners: List[EntityOwnerDestination], **kwargs):
        """
        Attributes for generating team campaign reports.

        :param entity_owners: List of entity owners and their Slack destinations.
        :type entity_owners: [EntityOwnerDestination]
        """
        super().__init__(kwargs)

        self_.entity_owners = entity_owners
