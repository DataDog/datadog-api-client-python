# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_batch_migration_published_resource_status import (
        SecurityMonitoringBatchMigrationPublishedResourceStatus,
    )


class SecurityMonitoringBatchMigrationPublishedResourceAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_batch_migration_published_resource_status import (
            SecurityMonitoringBatchMigrationPublishedResourceStatus,
        )

        return {
            "error": (str,),
            "rule_id": (str,),
            "status": (SecurityMonitoringBatchMigrationPublishedResourceStatus,),
        }

    attribute_map = {
        "error": "error",
        "rule_id": "ruleId",
        "status": "status",
    }

    def __init__(
        self_,
        status: SecurityMonitoringBatchMigrationPublishedResourceStatus,
        error: Union[str, UnsetType] = unset,
        rule_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the publication outcome of a batch migration resource.

        :param error: The reason why the resource could not be published.
        :type error: str, optional

        :param rule_id: The ID of the created Cloud SIEM detection rule.
        :type rule_id: str, optional

        :param status: The outcome of publishing a batch migration resource.
        :type status: SecurityMonitoringBatchMigrationPublishedResourceStatus
        """
        if error is not unset:
            kwargs["error"] = error
        if rule_id is not unset:
            kwargs["rule_id"] = rule_id
        super().__init__(kwargs)

        self_.status = status
