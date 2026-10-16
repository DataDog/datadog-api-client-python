# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringBatchMigrationStatus(ModelSimple):
    """
    The status of a batch migration. A batch migration is created as `draft` and moves to
        `in_progress` when started. It moves to `completed` once no resource is `pending` or
        `in_progress`, or to `canceled` when canceled.

    :param value: Must be one of ["draft", "in_progress", "canceled", "completed"].
    :type value: str
    """

    allowed_values = {
        "draft",
        "in_progress",
        "canceled",
        "completed",
    }
    DRAFT: ClassVar["SecurityMonitoringBatchMigrationStatus"]
    IN_PROGRESS: ClassVar["SecurityMonitoringBatchMigrationStatus"]
    CANCELED: ClassVar["SecurityMonitoringBatchMigrationStatus"]
    COMPLETED: ClassVar["SecurityMonitoringBatchMigrationStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringBatchMigrationStatus.DRAFT = SecurityMonitoringBatchMigrationStatus("draft")
SecurityMonitoringBatchMigrationStatus.IN_PROGRESS = SecurityMonitoringBatchMigrationStatus("in_progress")
SecurityMonitoringBatchMigrationStatus.CANCELED = SecurityMonitoringBatchMigrationStatus("canceled")
SecurityMonitoringBatchMigrationStatus.COMPLETED = SecurityMonitoringBatchMigrationStatus("completed")
