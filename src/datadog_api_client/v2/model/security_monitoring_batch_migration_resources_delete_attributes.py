# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


class SecurityMonitoringBatchMigrationResourcesDeleteAttributes(ModelNormal):
    validations = {
        "resource_ids": {
            "max_items": 1000,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "resource_ids": ([UUID],),
        }

    attribute_map = {
        "resource_ids": "resourceIds",
    }

    def __init__(self_, resource_ids: List[UUID], **kwargs):
        """
        Attributes of the resources to delete from a batch migration.

        :param resource_ids: Unique UUIDs of batch migration resources. From 1 to 1000 IDs.
        :type resource_ids: [UUID]
        """
        super().__init__(kwargs)

        self_.resource_ids = resource_ids
