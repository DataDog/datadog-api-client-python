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
    from datadog_api_client.v2.model.table_result_v2_data import TableResultV2Data


class TableResultV2(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.table_result_v2_data import TableResultV2Data

        return {
            "data": (TableResultV2Data,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[TableResultV2Data, UnsetType] = unset, **kwargs):
        """
        A reference table resource containing its full configuration and state.

        :param data: The data object containing the reference table configuration and state.
        :type data: TableResultV2Data, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
