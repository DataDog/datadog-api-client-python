# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List, Union

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


class ExperimentsSubjectTypeV2DTODataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "experiment_count": (int, none_type),
            "exposure_source_count": (int, none_type),
            "is_default": (bool,),
            "metric_sql_model_count": (int, none_type),
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
            "product_analytics_attribute": (str,),
            "protocol_count": (int, none_type),
            "updated_at": (datetime,),
            "warehouse_column_names": ([str],),
        }

    attribute_map = {
        "created_at": "created_at",
        "experiment_count": "experiment_count",
        "exposure_source_count": "exposure_source_count",
        "is_default": "is_default",
        "metric_sql_model_count": "metric_sql_model_count",
        "migration_metadata": "migration_metadata",
        "name": "name",
        "product_analytics_attribute": "product_analytics_attribute",
        "protocol_count": "protocol_count",
        "updated_at": "updated_at",
        "warehouse_column_names": "warehouse_column_names",
    }

    def __init__(
        self_,
        created_at: Union[datetime, UnsetType] = unset,
        experiment_count: Union[int, none_type, UnsetType] = unset,
        exposure_source_count: Union[int, none_type, UnsetType] = unset,
        is_default: Union[bool, UnsetType] = unset,
        metric_sql_model_count: Union[int, none_type, UnsetType] = unset,
        migration_metadata: Union[Any, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        product_analytics_attribute: Union[str, UnsetType] = unset,
        protocol_count: Union[int, none_type, UnsetType] = unset,
        updated_at: Union[datetime, UnsetType] = unset,
        warehouse_column_names: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Details of the subject type.

        :param created_at: Time when this resource was created.
        :type created_at: datetime, optional

        :param experiment_count: Number of experiments that reference this resource.
        :type experiment_count: int, none_type, optional

        :param exposure_source_count: Number of exposure sources that reference this subject type.
        :type exposure_source_count: int, none_type, optional

        :param is_default: Whether this is the organization's default subject type.
        :type is_default: bool, optional

        :param metric_sql_model_count: Number of metric SQL models that reference this subject type.
        :type metric_sql_model_count: int, none_type, optional

        :param migration_metadata: Metadata retained for resources imported from another system.
        :type migration_metadata: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param name: Display name of the subject type.
        :type name: str, optional

        :param product_analytics_attribute: Product Analytics attribute used to identify subjects of this type.
        :type product_analytics_attribute: str, optional

        :param protocol_count: Number of protocols that reference this subject type.
        :type protocol_count: int, none_type, optional

        :param updated_at: Time when this resource was last updated.
        :type updated_at: datetime, optional

        :param warehouse_column_names: Warehouse columns that identify subjects of this type.
        :type warehouse_column_names: [str], optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if experiment_count is not unset:
            kwargs["experiment_count"] = experiment_count
        if exposure_source_count is not unset:
            kwargs["exposure_source_count"] = exposure_source_count
        if is_default is not unset:
            kwargs["is_default"] = is_default
        if metric_sql_model_count is not unset:
            kwargs["metric_sql_model_count"] = metric_sql_model_count
        if migration_metadata is not unset:
            kwargs["migration_metadata"] = migration_metadata
        if name is not unset:
            kwargs["name"] = name
        if product_analytics_attribute is not unset:
            kwargs["product_analytics_attribute"] = product_analytics_attribute
        if protocol_count is not unset:
            kwargs["protocol_count"] = protocol_count
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if warehouse_column_names is not unset:
            kwargs["warehouse_column_names"] = warehouse_column_names
        super().__init__(kwargs)
