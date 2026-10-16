# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringBatchMigrationResourceStatus(ModelSimple):
    """
    The status of a batch migration resource. `completed` resources have a translation in
        `output` that is ready to be published. `duplicate` is reserved for future duplicate rule
        detection.

    :param value: Must be one of ["pending", "in_progress", "completed", "canceled", "failed", "publishing", "published", "duplicate"].
    :type value: str
    """

    allowed_values = {
        "pending",
        "in_progress",
        "completed",
        "canceled",
        "failed",
        "publishing",
        "published",
        "duplicate",
    }
    PENDING: ClassVar["SecurityMonitoringBatchMigrationResourceStatus"]
    IN_PROGRESS: ClassVar["SecurityMonitoringBatchMigrationResourceStatus"]
    COMPLETED: ClassVar["SecurityMonitoringBatchMigrationResourceStatus"]
    CANCELED: ClassVar["SecurityMonitoringBatchMigrationResourceStatus"]
    FAILED: ClassVar["SecurityMonitoringBatchMigrationResourceStatus"]
    PUBLISHING: ClassVar["SecurityMonitoringBatchMigrationResourceStatus"]
    PUBLISHED: ClassVar["SecurityMonitoringBatchMigrationResourceStatus"]
    DUPLICATE: ClassVar["SecurityMonitoringBatchMigrationResourceStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringBatchMigrationResourceStatus.PENDING = SecurityMonitoringBatchMigrationResourceStatus("pending")
SecurityMonitoringBatchMigrationResourceStatus.IN_PROGRESS = SecurityMonitoringBatchMigrationResourceStatus(
    "in_progress"
)
SecurityMonitoringBatchMigrationResourceStatus.COMPLETED = SecurityMonitoringBatchMigrationResourceStatus("completed")
SecurityMonitoringBatchMigrationResourceStatus.CANCELED = SecurityMonitoringBatchMigrationResourceStatus("canceled")
SecurityMonitoringBatchMigrationResourceStatus.FAILED = SecurityMonitoringBatchMigrationResourceStatus("failed")
SecurityMonitoringBatchMigrationResourceStatus.PUBLISHING = SecurityMonitoringBatchMigrationResourceStatus("publishing")
SecurityMonitoringBatchMigrationResourceStatus.PUBLISHED = SecurityMonitoringBatchMigrationResourceStatus("published")
SecurityMonitoringBatchMigrationResourceStatus.DUPLICATE = SecurityMonitoringBatchMigrationResourceStatus("duplicate")
