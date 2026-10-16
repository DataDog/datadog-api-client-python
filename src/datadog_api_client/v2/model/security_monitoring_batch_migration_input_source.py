# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringBatchMigrationInputSource(ModelSimple):
    """
    The origin of a batch migration. Always `batch_migration` for batch migrations
        created through this API.

    :param value: Must be one of ["batch_migration", "threat_hunting", "user"].
    :type value: str
    """

    allowed_values = {
        "batch_migration",
        "threat_hunting",
        "user",
    }
    BATCH_MIGRATION: ClassVar["SecurityMonitoringBatchMigrationInputSource"]
    THREAT_HUNTING: ClassVar["SecurityMonitoringBatchMigrationInputSource"]
    USER: ClassVar["SecurityMonitoringBatchMigrationInputSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringBatchMigrationInputSource.BATCH_MIGRATION = SecurityMonitoringBatchMigrationInputSource(
    "batch_migration"
)
SecurityMonitoringBatchMigrationInputSource.THREAT_HUNTING = SecurityMonitoringBatchMigrationInputSource(
    "threat_hunting"
)
SecurityMonitoringBatchMigrationInputSource.USER = SecurityMonitoringBatchMigrationInputSource("user")
