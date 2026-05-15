# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List, Union, TYPE_CHECKING

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


if TYPE_CHECKING:
    from datadog_api_client.v2.model.commitments_scalar_column_meta import CommitmentsScalarColumnMeta
    from datadog_api_client.v2.model.commitments_scalar_column_type import CommitmentsScalarColumnType


class CommitmentsScalarColumn(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.commitments_scalar_column_meta import CommitmentsScalarColumnMeta
        from datadog_api_client.v2.model.commitments_scalar_column_type import CommitmentsScalarColumnType

        return {
            "meta": (CommitmentsScalarColumnMeta,),
            "name": (str,),
            "type": (CommitmentsScalarColumnType,),
            "values": ([bool, date, datetime, dict, float, int, list, str, UUID, none_type],),
        }

    attribute_map = {
        "meta": "meta",
        "name": "name",
        "type": "type",
        "values": "values",
    }

    def __init__(
        self_,
        name: str,
        type: CommitmentsScalarColumnType,
        values: List[Any],
        meta: Union[CommitmentsScalarColumnMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        A column in a scalar response. When type is "group", values contains arrays of strings. When type is "number", values contains numeric values.

        :param meta: Metadata for a scalar column, including unit information.
        :type meta: CommitmentsScalarColumnMeta, optional

        :param name: The column name.
        :type name: str

        :param type: The column type. "group" for dimension columns, "number" for metric columns.
        :type type: CommitmentsScalarColumnType

        :param values: Values for a scalar column. Arrays of strings for group columns, numbers for value columns.
        :type values: [bool, date, datetime, dict, float, int, list, str, UUID, none_type]
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.name = name
        self_.type = type
        self_.values = values
