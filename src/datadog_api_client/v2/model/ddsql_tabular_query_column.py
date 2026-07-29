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

        :param values: Column values in row order, one entry per result row. The element type
            follows the column's ``type``. The following serialization rules should be
            taken into account:

            * ``BIGINT`` values are encoded as JSON numbers in the signed 64-bit integer range.
            * ``DECIMAL`` values are encoded as JSON numbers with 64-bit double precision.
            * ``TIMESTAMP`` and ``DATE`` values are encoded as Unix-millisecond integers; a
              ``DATE`` resolves to midnight UTC.
            * ``JSON`` values are returned as a JSON-encoded string.

            ``null`` is allowed for any column type where a value is missing.
        :type values: [bool, date, datetime, dict, float, int, list, str, UUID, none_type]
        """
        super().__init__(kwargs)

        self_.name = name
        self_.type = type
        self_.values = values
