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


class ExperimentsMetricSQLModelV2DTODataAttributesMeasuresItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_create_exposure_sql_model_v2_request_data_attributes_items_column_type import (
            ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType,
        )

        return {
            "column_name": (str,),
            "column_type": (ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType,),
            "description": (str,),
            "id": (str,),
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
            "name": (str,),
        }

    attribute_map = {
        "column_name": "column_name",
        "column_type": "column_type",
        "description": "description",
        "id": "id",
        "migration_metadata": "migration_metadata",
        "name": "name",
    }

    def __init__(
        self_,
        column_name: Union[str, UnsetType] = unset,
        column_type: Union[ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        migration_metadata: Union[Any, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A measure available from a metric SQL model column.

        :param column_name: Name of the SQL result column that supplies this measure.
        :type column_name: str, optional

        :param column_type: Data type of a column in the SQL model.
        :type column_type: ExperimentsCreateExposureSQLModelV2RequestDataAttributesItemsColumnType, optional

        :param description: Text that explains the measure.
        :type description: str, optional

        :param id: ID of the measure.
        :type id: str, optional

        :param migration_metadata: Metadata retained for resources imported from another system.
        :type migration_metadata: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param name: Display name of the measure.
        :type name: str, optional
        """
        if column_name is not unset:
            kwargs["column_name"] = column_name
        if column_type is not unset:
            kwargs["column_type"] = column_type
        if description is not unset:
            kwargs["description"] = description
        if id is not unset:
            kwargs["id"] = id
        if migration_metadata is not unset:
            kwargs["migration_metadata"] = migration_metadata
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
