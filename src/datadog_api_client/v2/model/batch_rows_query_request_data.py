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
    from datadog_api_client.v2.model.batch_rows_query_request_data_attributes import BatchRowsQueryRequestDataAttributes
    from datadog_api_client.v2.model.batch_rows_query_data_type import BatchRowsQueryDataType


class BatchRowsQueryRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.batch_rows_query_request_data_attributes import (
            BatchRowsQueryRequestDataAttributes,
        )
        from datadog_api_client.v2.model.batch_rows_query_data_type import BatchRowsQueryDataType

        return {
            "attributes": (BatchRowsQueryRequestDataAttributes,),
            "type": (BatchRowsQueryDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: BatchRowsQueryDataType,
        attributes: Union[BatchRowsQueryRequestDataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for a batch rows query request.

        :param attributes: Attributes for a batch rows query request.
        :type attributes: BatchRowsQueryRequestDataAttributes, optional

        :param type: Resource type identifier for batch queries of reference table rows.
        :type type: BatchRowsQueryDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
