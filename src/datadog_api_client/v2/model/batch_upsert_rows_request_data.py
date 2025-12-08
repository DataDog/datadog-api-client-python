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
    from datadog_api_client.v2.model.batch_upsert_rows_request_data_attributes import (
        BatchUpsertRowsRequestDataAttributes,
    )
    from datadog_api_client.v2.model.table_row_resource_data_type import TableRowResourceDataType


class BatchUpsertRowsRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.batch_upsert_rows_request_data_attributes import (
            BatchUpsertRowsRequestDataAttributes,
        )
        from datadog_api_client.v2.model.table_row_resource_data_type import TableRowResourceDataType

        return {
            "attributes": (BatchUpsertRowsRequestDataAttributes,),
            "id": (str,),
            "type": (TableRowResourceDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: TableRowResourceDataType,
        attributes: Union[BatchUpsertRowsRequestDataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Row resource containing a single row identifier and its column values.

        :param attributes: Attributes containing row data values for row creation or update operations.
        :type attributes: BatchUpsertRowsRequestDataAttributes, optional

        :param id:
        :type id: str

        :param type: Row resource type.
        :type type: TableRowResourceDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
