# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class TableRowResourceDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "values": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
        }

    attribute_map = {
        "values": "values",
    }

    def __init__(self_, values: Union[Dict[str, Any], UnsetType] = unset, **kwargs):
        """
        The definition of ``TableRowResourceDataAttributes`` object.

        :param values: The values of the row.
        :type values: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional
        """
        if values is not unset:
            kwargs["values"] = values
        super().__init__(kwargs)
