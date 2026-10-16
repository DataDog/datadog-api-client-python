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
    from datadog_api_client.v2.model.security_monitoring_batch_migration_resource_input_type import (
        SecurityMonitoringBatchMigrationResourceInputType,
    )


class SecurityMonitoringBatchMigrationResourceCreateItem(ModelNormal):
    validations = {
        "description": {
            "max_length": 4096,
        },
        "input": {
            "max_length": 65536,
            "min_length": 1,
        },
        "name": {
            "max_length": 512,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_batch_migration_resource_input_type import (
            SecurityMonitoringBatchMigrationResourceInputType,
        )

        return {
            "description": (str,),
            "input": (str,),
            "input_type": (SecurityMonitoringBatchMigrationResourceInputType,),
            "name": (str,),
        }

    attribute_map = {
        "description": "description",
        "input": "input",
        "input_type": "inputType",
        "name": "name",
    }

    def __init__(
        self_,
        input: str,
        input_type: SecurityMonitoringBatchMigrationResourceInputType,
        description: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A source rule to translate into a Cloud SIEM detection rule.

        :param description: The description of the resource.
        :type description: str, optional

        :param input: The source query or natural language description to translate. Must not be blank.
        :type input: str

        :param input_type: The type of the source rule: ``spl`` for a Splunk SPL search or saved search definition,
            ``natural_language`` for a plain-English description of the behavior to detect, or ``kql``
            for a Microsoft KQL query. SPL inputs must be self-contained, with search macros expanded.
        :type input_type: SecurityMonitoringBatchMigrationResourceInputType

        :param name: The name of the resource.
        :type name: str, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.input = input
        self_.input_type = input_type
