# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class TableRowResourceDataAttributes(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "values": (dict,),
        }

    attribute_map = {
        "values": "values",
    }

    def __init__(self_, values: Union[dict, UnsetType] = unset, **kwargs):
        """
        Column values for this row in the reference table.

        :param values: Key-value pairs representing the row data, where keys are field names from the schema.
        :type values: dict, optional
        """
        if values is not unset:
            kwargs["values"] = values
        super().__init__(kwargs)
