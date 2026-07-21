# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    UUID,
)


class DdsqlTabularQueryColumn(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "type": (str,),
            "values": ([bool, date, datetime, dict, float, int, list, str, UUID, none_type],),
        }

    attribute_map = {
        "name": "name",
        "type": "type",
        "values": "values",
    }

    def __init__(self_, name: str, type: str, values: List[Any], **kwargs):
        """
        A single column of a DDSQL tabular query result.

        :param name: Name of the column as projected by the SQL statement.
        :type name: str

        :param type: DDSQL data type of the column's values, for example ``VARCHAR`` , ``BIGINT`` ,
            ``DECIMAL`` , ``BOOLEAN`` , ``TIMESTAMP`` , ``JSON`` , or an array variant such as
            ``VARCHAR[]``. See the
            `DDSQL data-types reference <https://docs.datadoghq.com/ddsql_reference/#data-types>`_
            for the full, up-to-date list.
        :type type: str

        :param values: Column values in row order. The element type matches the column's ``type`` ;
            for example a ``VARCHAR`` column carries strings, a ``TIMESTAMP`` column carries
            Unix-millisecond integers. ``null`` is allowed for missing values.
        :type values: [bool, date, datetime, dict, float, int, list, str, UUID, none_type]
        """
        super().__init__(kwargs)

        self_.name = name
        self_.type = type
        self_.values = values
