# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.dataset_sort_field import DatasetSortField


class DatasetListQuerySort(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.dataset_sort_field import DatasetSortField

        return {
            "fields": ([DatasetSortField],),
        }

    attribute_map = {
        "fields": "fields",
    }

    def __init__(self_, fields: List[DatasetSortField], **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param fields: Test-only generated schema for the dashboard versioning proof of concept.
        :type fields: [DatasetSortField]
        """
        super().__init__(kwargs)

        self_.fields = fields
