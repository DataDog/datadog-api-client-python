# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.legacy_formula_backed_data_projection_source import (
        LegacyFormulaBackedDataProjectionSource,
    )
    from datadog_api_client.v1_20270101.model.storage_type import StorageType


class EventsPlatformDataProjectionQueryDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.legacy_formula_backed_data_projection_source import (
            LegacyFormulaBackedDataProjectionSource,
        )
        from datadog_api_client.v1_20270101.model.storage_type import StorageType

        return {
            "data_source": (LegacyFormulaBackedDataProjectionSource,),
            "indexes": ([str],),
            "query_string": (str,),
            "storage": (StorageType,),
        }

    attribute_map = {
        "data_source": "data_source",
        "indexes": "indexes",
        "query_string": "query_string",
        "storage": "storage",
    }

    def __init__(
        self_,
        data_source: LegacyFormulaBackedDataProjectionSource,
        query_string: str,
        indexes: Union[List[str], UnsetType] = unset,
        storage: Union[StorageType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: LegacyFormulaBackedDataProjectionSource

        :param indexes: Test-only generated schema for the dashboard versioning proof of concept.
        :type indexes: [str], optional

        :param query_string: Test-only generated schema for the dashboard versioning proof of concept.
        :type query_string: str

        :param storage: Test-only generated schema for the dashboard versioning proof of concept.
        :type storage: StorageType, optional
        """
        if indexes is not unset:
            kwargs["indexes"] = indexes
        if storage is not unset:
            kwargs["storage"] = storage
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.query_string = query_string
