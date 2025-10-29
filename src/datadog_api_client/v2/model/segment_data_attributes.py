# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.segment_data_source import SegmentDataSource
    from datadog_api_client.v2.model.segment_data_attributes_data_query import SegmentDataAttributesDataQuery


class SegmentDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.segment_data_source import SegmentDataSource
        from datadog_api_client.v2.model.segment_data_attributes_data_query import SegmentDataAttributesDataQuery

        return {
            "created_at": (datetime,),
            "created_by": (SegmentDataSource,),
            "data_query": (SegmentDataAttributesDataQuery,),
            "description": (str,),
            "disabled_at": (datetime,),
            "disabled_by": (SegmentDataSource,),
            "materialization_row_count": (int,),
            "materialized_at": (str,),
            "modified_at": (datetime,),
            "modified_by": (SegmentDataSource,),
            "name": (str,),
            "org_id": (int,),
            "source": (int,),
            "tags": ([str],),
            "version": (int,),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "data_query": "data_query",
        "description": "description",
        "disabled_at": "disabled_at",
        "disabled_by": "disabled_by",
        "materialization_row_count": "materialization_row_count",
        "materialized_at": "materialized_at",
        "modified_at": "modified_at",
        "modified_by": "modified_by",
        "name": "name",
        "org_id": "org_id",
        "source": "source",
        "tags": "tags",
        "version": "version",
    }

    def __init__(
        self_,
        data_query: SegmentDataAttributesDataQuery,
        name: str,
        created_at: Union[datetime, UnsetType] = unset,
        created_by: Union[SegmentDataSource, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        disabled_at: Union[datetime, UnsetType] = unset,
        disabled_by: Union[SegmentDataSource, UnsetType] = unset,
        materialization_row_count: Union[int, UnsetType] = unset,
        materialized_at: Union[str, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        modified_by: Union[SegmentDataSource, UnsetType] = unset,
        org_id: Union[int, UnsetType] = unset,
        source: Union[int, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        version: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param created_at:
        :type created_at: datetime, optional

        :param created_by:
        :type created_by: SegmentDataSource, optional

        :param data_query:
        :type data_query: SegmentDataAttributesDataQuery

        :param description:
        :type description: str, optional

        :param disabled_at:
        :type disabled_at: datetime, optional

        :param disabled_by:
        :type disabled_by: SegmentDataSource, optional

        :param materialization_row_count:
        :type materialization_row_count: int, optional

        :param materialized_at:
        :type materialized_at: str, optional

        :param modified_at:
        :type modified_at: datetime, optional

        :param modified_by:
        :type modified_by: SegmentDataSource, optional

        :param name:
        :type name: str

        :param org_id:
        :type org_id: int, optional

        :param source:
        :type source: int, optional

        :param tags:
        :type tags: [str], optional

        :param version:
        :type version: int, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if description is not unset:
            kwargs["description"] = description
        if disabled_at is not unset:
            kwargs["disabled_at"] = disabled_at
        if disabled_by is not unset:
            kwargs["disabled_by"] = disabled_by
        if materialization_row_count is not unset:
            kwargs["materialization_row_count"] = materialization_row_count
        if materialized_at is not unset:
            kwargs["materialized_at"] = materialized_at
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if modified_by is not unset:
            kwargs["modified_by"] = modified_by
        if org_id is not unset:
            kwargs["org_id"] = org_id
        if source is not unset:
            kwargs["source"] = source
        if tags is not unset:
            kwargs["tags"] = tags
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)

        self_.data_query = data_query
        self_.name = name
