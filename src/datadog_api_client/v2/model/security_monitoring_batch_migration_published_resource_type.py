# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringBatchMigrationPublishedResourceType(ModelSimple):
    """
    The type of resource for a published batch migration resource.

    :param value: If omitted defaults to "batchMigrationPublishedResource". Must be one of ["batchMigrationPublishedResource"].
    :type value: str
    """

    allowed_values = {
        "batchMigrationPublishedResource",
    }
    BATCH_MIGRATION_PUBLISHED_RESOURCE: ClassVar["SecurityMonitoringBatchMigrationPublishedResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringBatchMigrationPublishedResourceType.BATCH_MIGRATION_PUBLISHED_RESOURCE = (
    SecurityMonitoringBatchMigrationPublishedResourceType("batchMigrationPublishedResource")
)
