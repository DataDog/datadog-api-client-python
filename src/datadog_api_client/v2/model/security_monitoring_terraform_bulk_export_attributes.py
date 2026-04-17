# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringTerraformBulkExportAttributes(ModelNormal):
    validations = {
        "resource_ids": {
            "max_items": 1000,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "resource_ids": ([str],),
        }

    attribute_map = {
        "resource_ids": "resource_ids",
    }

    def __init__(self_, resource_ids: List[str], **kwargs):
        """
        Attributes for the bulk export request.

        :param resource_ids: The list of resource IDs to export. Maximum 1000 items.
        :type resource_ids: [str]
        """
        super().__init__(kwargs)

        self_.resource_ids = resource_ids
