# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.batch_upsert_rows_request_data_attributes_value import (
        BatchUpsertRowsRequestDataAttributesValue,
    )


class BatchUpsertRowsRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.batch_upsert_rows_request_data_attributes_value import (
            BatchUpsertRowsRequestDataAttributesValue,
        )

        return {
            "values": ({str: (BatchUpsertRowsRequestDataAttributesValue,)},),
        }

    attribute_map = {
        "values": "values",
    }

    def __init__(self_, values: Dict[str, Union[BatchUpsertRowsRequestDataAttributesValue, str, int]], **kwargs):
        """
        Attributes containing row data values for row creation or update operations.

        :param values: Key-value pairs representing row data, where keys are schema field names and values match the corresponding column types.
        :type values: {str: (BatchUpsertRowsRequestDataAttributesValue,)}
        """
        super().__init__(kwargs)

        self_.values = values
