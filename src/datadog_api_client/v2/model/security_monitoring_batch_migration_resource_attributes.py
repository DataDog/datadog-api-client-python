# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_batch_migration_resource_input_type import (
        SecurityMonitoringBatchMigrationResourceInputType,
    )
    from datadog_api_client.v2.model.security_monitoring_batch_migration_resource_output import (
        SecurityMonitoringBatchMigrationResourceOutput,
    )
    from datadog_api_client.v2.model.security_monitoring_batch_migration_resource_status import (
        SecurityMonitoringBatchMigrationResourceStatus,
    )


class SecurityMonitoringBatchMigrationResourceAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_batch_migration_resource_input_type import (
            SecurityMonitoringBatchMigrationResourceInputType,
        )
        from datadog_api_client.v2.model.security_monitoring_batch_migration_resource_output import (
            SecurityMonitoringBatchMigrationResourceOutput,
        )
        from datadog_api_client.v2.model.security_monitoring_batch_migration_resource_status import (
            SecurityMonitoringBatchMigrationResourceStatus,
        )

        return {
            "batch_id": (UUID,),
            "created_at": (datetime,),
            "created_by": (str,),
            "description": (str,),
            "input": (str,),
            "input_type": (SecurityMonitoringBatchMigrationResourceInputType,),
            "last_updated_at": (datetime,),
            "last_updated_by": (str,),
            "name": (str,),
            "output": (SecurityMonitoringBatchMigrationResourceOutput,),
            "output_type": (str,),
            "rule_id": (str,),
            "status": (SecurityMonitoringBatchMigrationResourceStatus,),
        }

    attribute_map = {
        "batch_id": "batchId",
        "created_at": "createdAt",
        "created_by": "createdBy",
        "description": "description",
        "input": "input",
        "input_type": "inputType",
        "last_updated_at": "lastUpdatedAt",
        "last_updated_by": "lastUpdatedBy",
        "name": "name",
        "output": "output",
        "output_type": "outputType",
        "rule_id": "ruleId",
        "status": "status",
    }

    def __init__(
        self_,
        batch_id: UUID,
        created_at: datetime,
        input: str,
        input_type: SecurityMonitoringBatchMigrationResourceInputType,
        last_updated_at: datetime,
        name: str,
        output: Union[SecurityMonitoringBatchMigrationResourceOutput, none_type],
        output_type: str,
        status: SecurityMonitoringBatchMigrationResourceStatus,
        created_by: Union[str, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        last_updated_by: Union[str, UnsetType] = unset,
        rule_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a batch migration resource.

        :param batch_id: The UUID of the batch migration that contains the resource.
        :type batch_id: UUID

        :param created_at: The creation date of the resource, in RFC 3339 format.
        :type created_at: datetime

        :param created_by: The UUID of the user or service account who created the resource.
        :type created_by: str, optional

        :param description: The description of the resource.
        :type description: str, optional

        :param input: The source query or natural language description to translate.
        :type input: str

        :param input_type: The type of the source rule: ``spl`` for a Splunk SPL search or saved search definition,
            ``natural_language`` for a plain-English description of the behavior to detect, or ``kql``
            for a Microsoft KQL query. SPL inputs must be self-contained, with search macros expanded.
        :type input_type: SecurityMonitoringBatchMigrationResourceInputType

        :param last_updated_at: The last update date of the resource, in RFC 3339 format.
        :type last_updated_at: datetime

        :param last_updated_by: The UUID of the user or service account who last updated the resource,
            or the name of a system actor.
        :type last_updated_by: str, optional

        :param name: The name of the resource.
        :type name: str

        :param output: The translation output. When the resource is ``completed`` , a Cloud SIEM detection rule
            definition in the same format as the create detection rule API. When the resource is
            ``failed`` , an object with an ``error`` describing the failure, with ``kind`` set to
            ``translation_error`` or ``internal_error`` , and optional ``type`` and ``message``. Otherwise, null.
        :type output: SecurityMonitoringBatchMigrationResourceOutput, none_type

        :param output_type: The type of the translation output. Currently always ``siem_rule``.
        :type output_type: str

        :param rule_id: The ID of the Cloud SIEM detection rule created when the resource was published.
        :type rule_id: str, optional

        :param status: The status of a batch migration resource. ``completed`` resources have a translation in
            ``output`` that is ready to be published. ``duplicate`` is reserved for future duplicate rule
            detection.
        :type status: SecurityMonitoringBatchMigrationResourceStatus
        """
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if description is not unset:
            kwargs["description"] = description
        if last_updated_by is not unset:
            kwargs["last_updated_by"] = last_updated_by
        if rule_id is not unset:
            kwargs["rule_id"] = rule_id
        super().__init__(kwargs)

        self_.batch_id = batch_id
        self_.created_at = created_at
        self_.input = input
        self_.input_type = input_type
        self_.last_updated_at = last_updated_at
        self_.name = name
        self_.output = output
        self_.output_type = output_type
        self_.status = status
