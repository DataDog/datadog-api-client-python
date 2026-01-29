# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_dataset_definition_column import (
        SecurityMonitoringDatasetDefinitionColumn,
    )


class SecurityMonitoringDatasetDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_dataset_definition_column import (
            SecurityMonitoringDatasetDefinitionColumn,
        )

        return {
            "columns": ([SecurityMonitoringDatasetDefinitionColumn],),
            "data_source": (str,),
            "indexes": ([str],),
            "name": (str,),
        }

    attribute_map = {
        "columns": "columns",
        "data_source": "data_source",
        "indexes": "indexes",
        "name": "name",
    }

    def __init__(
        self_,
        columns: List[SecurityMonitoringDatasetDefinitionColumn],
        data_source: str,
        name: str,
        indexes: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of a dataset, including its data source, name, indexes, and columns.

        :param columns: The columns in the dataset.
        :type columns: [SecurityMonitoringDatasetDefinitionColumn]

        :param data_source: The data source for the dataset.
        :type data_source: str

        :param indexes: The indexes to use for the dataset.
        :type indexes: [str], optional

        :param name: The name of the dataset. Must start with a letter, contain only lowercase letters, numbers, and underscores, and be at most 255 characters long.
        :type name: str
        """
        if indexes is not unset:
            kwargs["indexes"] = indexes
        super().__init__(kwargs)

        self_.columns = columns
        self_.data_source = data_source
        self_.name = name
