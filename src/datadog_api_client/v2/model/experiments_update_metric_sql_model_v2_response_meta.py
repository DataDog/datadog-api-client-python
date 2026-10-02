# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ExperimentsUpdateMetricSQLModelV2ResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "deleted_measures": ([str],),
            "deleted_properties": ([str],),
            "deleted_subject_types": ([str],),
        }

    attribute_map = {
        "deleted_measures": "deleted_measures",
        "deleted_properties": "deleted_properties",
        "deleted_subject_types": "deleted_subject_types",
    }

    def __init__(
        self_,
        deleted_measures: Union[List[str], UnsetType] = unset,
        deleted_properties: Union[List[str], UnsetType] = unset,
        deleted_subject_types: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Model entries removed by the update. Empty arrays mean no entries were removed.

        :param deleted_measures: Measure column names removed from the model.
        :type deleted_measures: [str], optional

        :param deleted_properties: Property names removed from the model.
        :type deleted_properties: [str], optional

        :param deleted_subject_types: Subject type IDs removed from the model.
        :type deleted_subject_types: [str], optional
        """
        if deleted_measures is not unset:
            kwargs["deleted_measures"] = deleted_measures
        if deleted_properties is not unset:
            kwargs["deleted_properties"] = deleted_properties
        if deleted_subject_types is not unset:
            kwargs["deleted_subject_types"] = deleted_subject_types
        super().__init__(kwargs)
