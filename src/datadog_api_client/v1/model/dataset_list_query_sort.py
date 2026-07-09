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
    from datadog_api_client.v1.model.dataset_list_query_sort_field import DatasetListQuerySortField


class DatasetListQuerySort(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.dataset_list_query_sort_field import DatasetListQuerySortField

        return {
            "fields": ([DatasetListQuerySortField],),
        }

    attribute_map = {
        "fields": "fields",
    }

    def __init__(self_, fields: List[DatasetListQuerySortField], **kwargs):
        """
        Sort configuration for a ``DatasetListQuery``.

        :param fields: List of fields to sort the rows by, applied in order.
        :type fields: [DatasetListQuerySortField]
        """
        super().__init__(kwargs)

        self_.fields = fields
