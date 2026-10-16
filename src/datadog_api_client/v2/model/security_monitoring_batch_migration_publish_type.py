# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringBatchMigrationPublishType(ModelSimple):
    """
    The type of resource for a batch migration publish request.

    :param value: If omitted defaults to "batchMigrationPublish". Must be one of ["batchMigrationPublish"].
    :type value: str
    """

    allowed_values = {
        "batchMigrationPublish",
    }
    BATCH_MIGRATION_PUBLISH: ClassVar["SecurityMonitoringBatchMigrationPublishType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringBatchMigrationPublishType.BATCH_MIGRATION_PUBLISH = SecurityMonitoringBatchMigrationPublishType(
    "batchMigrationPublish"
)
