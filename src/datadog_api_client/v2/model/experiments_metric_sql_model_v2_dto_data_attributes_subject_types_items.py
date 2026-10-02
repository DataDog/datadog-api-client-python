# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ExperimentsMetricSQLModelV2DTODataAttributesSubjectTypesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "column_name": (str,),
            "subject_type_id": (str,),
            "unique_subject_count_measure_id": (str,),
        }

    attribute_map = {
        "column_name": "column_name",
        "subject_type_id": "subject_type_id",
        "unique_subject_count_measure_id": "unique_subject_count_measure_id",
    }

    def __init__(
        self_,
        column_name: Union[str, UnsetType] = unset,
        subject_type_id: Union[str, UnsetType] = unset,
        unique_subject_count_measure_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A mapping between a subject type and its identifying SQL column.

        :param column_name: Name of the SQL result column that identifies subjects of this type.
        :type column_name: str, optional

        :param subject_type_id: ID of the subject type used by this configuration.
        :type subject_type_id: str, optional

        :param unique_subject_count_measure_id: Read-only measure ID. Pass it as warehouse_metric_measure.id when the metric operation is ``uniqueSubjects``.
        :type unique_subject_count_measure_id: str, optional
        """
        if column_name is not unset:
            kwargs["column_name"] = column_name
        if subject_type_id is not unset:
            kwargs["subject_type_id"] = subject_type_id
        if unique_subject_count_measure_id is not unset:
            kwargs["unique_subject_count_measure_id"] = unique_subject_count_measure_id
        super().__init__(kwargs)
