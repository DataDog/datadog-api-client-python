# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    UUID,
)


class BatchUpsertRowsRequestDataAttributes(ModelNormal):
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

    def __init__(self_, values: Dict[str, Any], **kwargs):
        """
        Attributes containing row data values for row creation or update operations.

        :param values: Key-value pairs representing row data, where keys are field names from the schema.
        :type values: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}
        """
        super().__init__(kwargs)

        self_.values = values
