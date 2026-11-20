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
    from datadog_api_client.v1_20270101.model.dataset_column import DatasetColumn
    from datadog_api_client.v1_20270101.model.actions_datastore_dataset_data_source import (
        ActionsDatastoreDatasetDataSource,
    )


class ActionsDatastoreDataset(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.dataset_column import DatasetColumn
        from datadog_api_client.v1_20270101.model.actions_datastore_dataset_data_source import (
            ActionsDatastoreDatasetDataSource,
        )

        return {
            "columns": ([DatasetColumn],),
            "data_source": (ActionsDatastoreDatasetDataSource,),
            "id": (str,),
            "name": (str,),
        }

    attribute_map = {
        "columns": "columns",
        "data_source": "data_source",
        "id": "id",
        "name": "name",
    }

    def __init__(
        self_,
        columns: List[DatasetColumn],
        data_source: ActionsDatastoreDatasetDataSource,
        id: str,
        name: str,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [DatasetColumn]

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: ActionsDatastoreDatasetDataSource

        :param id: Test-only generated schema for the dashboard versioning proof of concept.
        :type id: str

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str
        """
        super().__init__(kwargs)

        self_.columns = columns
        self_.data_source = data_source
        self_.id = id
        self_.name = name
