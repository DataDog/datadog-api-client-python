# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_dataset_definition_column_type import (
        SecurityMonitoringDatasetDefinitionColumnType,
    )


class SecurityMonitoringDatasetDefinitionColumn(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_dataset_definition_column_type import (
            SecurityMonitoringDatasetDefinitionColumnType,
        )

        return {
            "column": (str,),
            "type": (SecurityMonitoringDatasetDefinitionColumnType,),
        }

    attribute_map = {
        "column": "column",
        "type": "type",
    }

    def __init__(self_, column: str, type: SecurityMonitoringDatasetDefinitionColumnType, **kwargs):
        """
        A column in a dataset definition.

        :param column: The name of the column.
        :type column: str

        :param type: The type of the column in a dataset definition.
        :type type: SecurityMonitoringDatasetDefinitionColumnType
        """
        super().__init__(kwargs)

        self_.column = column
        self_.type = type
