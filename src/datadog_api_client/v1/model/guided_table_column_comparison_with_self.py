# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.guided_table_column_comparison_with_self_type import (
        GuidedTableColumnComparisonWithSelfType,
    )


class GuidedTableColumnComparisonWithSelf(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.guided_table_column_comparison_with_self_type import (
            GuidedTableColumnComparisonWithSelfType,
        )

        return {
            "type": (GuidedTableColumnComparisonWithSelfType,),
        }

    attribute_map = {
        "type": "type",
    }

    def __init__(self_, type: GuidedTableColumnComparisonWithSelfType, **kwargs):
        """
        Comparison of a column value against the column's own total (percent of column total).

        :param type:
        :type type: GuidedTableColumnComparisonWithSelfType
        """
        super().__init__(kwargs)

        self_.type = type
