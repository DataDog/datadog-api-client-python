# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.batch_rows_query_response_data_relationships import (
        BatchRowsQueryResponseDataRelationships,
    )
    from datadog_api_client.v2.model.batch_rows_query_data_type import BatchRowsQueryDataType


class BatchRowsQueryResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.batch_rows_query_response_data_relationships import (
            BatchRowsQueryResponseDataRelationships,
        )
        from datadog_api_client.v2.model.batch_rows_query_data_type import BatchRowsQueryDataType

        return {
            "id": (str,),
            "relationships": (BatchRowsQueryResponseDataRelationships,),
            "type": (BatchRowsQueryDataType,),
        }

    attribute_map = {
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        type: BatchRowsQueryDataType,
        id: Union[str, UnsetType] = unset,
        relationships: Union[BatchRowsQueryResponseDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for a batch rows query response.

        :param id: Unique identifier of the batch query.
        :type id: str, optional

        :param relationships: Relationships of the batch rows query response data.
        :type relationships: BatchRowsQueryResponseDataRelationships, optional

        :param type: Resource type identifier for batch queries of reference table rows.
        :type type: BatchRowsQueryDataType
        """
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
