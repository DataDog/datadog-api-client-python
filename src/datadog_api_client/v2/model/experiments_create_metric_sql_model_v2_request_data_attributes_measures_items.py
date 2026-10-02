# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_create_exposure_sql_model_v2_request_data_attributes_items_column_type import (
        ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType,
    )


class ExperimentsCreateMetricSQLModelV2RequestDataAttributesMeasuresItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_create_exposure_sql_model_v2_request_data_attributes_items_column_type import (
            ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType,
        )

        return {
            "column_name": (str,),
            "column_type": (ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType,),
            "description": (str, none_type),
            "migration_metadata": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
            "name": (str, none_type),
        }

    attribute_map = {
        "column_name": "column_name",
        "column_type": "column_type",
        "description": "description",
        "migration_metadata": "migration_metadata",
        "name": "name",
    }

    def __init__(
        self_,
        column_name: str,
        column_type: ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType,
        description: Union[str, none_type, UnsetType] = unset,
        migration_metadata: Union[Any, UnsetType] = unset,
        name: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Column in the SQL model that supplies values for a metric measure.

        :param column_name: SQL result column that contains the measure values.
        :type column_name: str

        :param column_type: Data type of a column in the SQL model.
        :type column_type: ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType

        :param description: Description of the measure.
        :type description: str, none_type, optional

        :param migration_metadata: Metadata associated with migration of this resource.
        :type migration_metadata: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param name: Display name of the measure.
        :type name: str, none_type, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if migration_metadata is not unset:
            kwargs["migration_metadata"] = migration_metadata
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.column_name = column_name
        self_.column_type = column_type
