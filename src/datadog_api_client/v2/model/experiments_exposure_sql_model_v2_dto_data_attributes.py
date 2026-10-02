# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List, Union, TYPE_CHECKING

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
    from datadog_api_client.v2.model.experiments_exposure_sql_model_v2_dto_data_attributes_items import (
        ExperimentsExposureSQLModelV2DTODataAttributesItems,
    )
    from datadog_api_client.v2.model.experiments_create_exposure_sql_model_v2_request_data_attributes_subject_types_items import (
        ExperimentsCreateExposureSQLModelV2RequestDataAttributesSubjectTypesItems,
    )


class ExperimentsExposureSQLModelV2DTODataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_exposure_sql_model_v2_dto_data_attributes_items import (
            ExperimentsExposureSQLModelV2DTODataAttributesItems,
        )
        from datadog_api_client.v2.model.experiments_create_exposure_sql_model_v2_request_data_attributes_subject_types_items import (
            ExperimentsCreateExposureSQLModelV2RequestDataAttributesSubjectTypesItems,
        )

        return {
            "archived_at": (datetime, none_type),
            "created_at": (datetime,),
            "date_partition_column": (str, none_type),
            "experiment_column": (str,),
            "experiment_count": (int, none_type),
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
            "properties": ([ExperimentsExposureSQLModelV2DTODataAttributesItems],),
            "sql": (str,),
            "subject_types": ([ExperimentsCreateExposureSQLModelV2RequestDataAttributesSubjectTypesItems],),
            "timestamp_column": (str,),
            "updated_at": (datetime,),
            "variant_column": (str,),
        }

    attribute_map = {
        "archived_at": "archived_at",
        "created_at": "created_at",
        "date_partition_column": "date_partition_column",
        "experiment_column": "experiment_column",
        "experiment_count": "experiment_count",
        "migration_metadata": "migration_metadata",
        "name": "name",
        "properties": "properties",
        "sql": "sql",
        "subject_types": "subject_types",
        "timestamp_column": "timestamp_column",
        "updated_at": "updated_at",
        "variant_column": "variant_column",
    }

    def __init__(
        self_,
        archived_at: Union[datetime, none_type, UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        date_partition_column: Union[str, none_type, UnsetType] = unset,
        experiment_column: Union[str, UnsetType] = unset,
        experiment_count: Union[int, none_type, UnsetType] = unset,
        migration_metadata: Union[Any, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        properties: Union[List[ExperimentsExposureSQLModelV2DTODataAttributesItems], UnsetType] = unset,
        sql: Union[str, UnsetType] = unset,
        subject_types: Union[
            List[ExperimentsCreateExposureSQLModelV2RequestDataAttributesSubjectTypesItems], UnsetType
        ] = unset,
        timestamp_column: Union[str, UnsetType] = unset,
        updated_at: Union[datetime, UnsetType] = unset,
        variant_column: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Query and column mappings used to read experiment assignment data.

        :param archived_at: Time when the exposure SQL model was archived.
        :type archived_at: datetime, none_type, optional

        :param created_at: Time when the exposure SQL model was created.
        :type created_at: datetime, optional

        :param date_partition_column: Column used to identify date partitions in the exposure data.
        :type date_partition_column: str, none_type, optional

        :param experiment_column: SQL result column that contains the experiment key.
        :type experiment_column: str, optional

        :param experiment_count: Number of experiments associated with the exposure SQL model.
        :type experiment_count: int, none_type, optional

        :param migration_metadata: Metadata associated with migration of this resource.
        :type migration_metadata: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param name: Display name of the exposure SQL model.
        :type name: str, optional

        :param properties: Property columns available for filtering or splitting exposure data.
        :type properties: [ExperimentsExposureSQLModelV2DTODataAttributesItems], optional

        :param sql: SQL query that supplies the experiment assignment data.
        :type sql: str, optional

        :param subject_types: Mappings between subject types and their identifier columns.
        :type subject_types: [ExperimentsCreateExposureSQLModelV2RequestDataAttributesSubjectTypesItems], optional

        :param timestamp_column: SQL result column that contains the assignment timestamp.
        :type timestamp_column: str, optional

        :param updated_at: Time when the exposure SQL model was last updated.
        :type updated_at: datetime, optional

        :param variant_column: SQL result column that contains the assigned variant.
        :type variant_column: str, optional
        """
        if archived_at is not unset:
            kwargs["archived_at"] = archived_at
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if date_partition_column is not unset:
            kwargs["date_partition_column"] = date_partition_column
        if experiment_column is not unset:
            kwargs["experiment_column"] = experiment_column
        if experiment_count is not unset:
            kwargs["experiment_count"] = experiment_count
        if migration_metadata is not unset:
            kwargs["migration_metadata"] = migration_metadata
        if name is not unset:
            kwargs["name"] = name
        if properties is not unset:
            kwargs["properties"] = properties
        if sql is not unset:
            kwargs["sql"] = sql
        if subject_types is not unset:
            kwargs["subject_types"] = subject_types
        if timestamp_column is not unset:
            kwargs["timestamp_column"] = timestamp_column
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if variant_column is not unset:
            kwargs["variant_column"] = variant_column
        super().__init__(kwargs)
