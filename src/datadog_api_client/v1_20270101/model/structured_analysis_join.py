# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.structured_analysis_join_condition import StructuredAnalysisJoinCondition
    from datadog_api_client.v1_20270101.model.structured_analysis_join_join_type import StructuredAnalysisJoinJoinType
    from datadog_api_client.v1_20270101.model.structured_analysis_join_type import StructuredAnalysisJoinType


class StructuredAnalysisJoin(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.structured_analysis_join_condition import (
            StructuredAnalysisJoinCondition,
        )
        from datadog_api_client.v1_20270101.model.structured_analysis_join_join_type import (
            StructuredAnalysisJoinJoinType,
        )
        from datadog_api_client.v1_20270101.model.structured_analysis_join_type import StructuredAnalysisJoinType

        return {
            "join_conditions": ([StructuredAnalysisJoinCondition],),
            "join_type": (StructuredAnalysisJoinJoinType,),
            "target_columns": ([str],),
            "target_dataset": (str,),
            "type": (StructuredAnalysisJoinType,),
        }

    attribute_map = {
        "join_conditions": "join_conditions",
        "join_type": "join_type",
        "target_columns": "target_columns",
        "target_dataset": "target_dataset",
        "type": "type",
    }

    def __init__(
        self_,
        join_conditions: List[StructuredAnalysisJoinCondition],
        join_type: StructuredAnalysisJoinJoinType,
        target_columns: List[str],
        target_dataset: str,
        type: StructuredAnalysisJoinType,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param join_conditions: Test-only generated schema for the dashboard versioning proof of concept.
        :type join_conditions: [StructuredAnalysisJoinCondition]

        :param join_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type join_type: StructuredAnalysisJoinJoinType

        :param target_columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type target_columns: [str]

        :param target_dataset: Test-only generated schema for the dashboard versioning proof of concept.
        :type target_dataset: str

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: StructuredAnalysisJoinType
        """
        super().__init__(kwargs)

        self_.join_conditions = join_conditions
        self_.join_type = join_type
        self_.target_columns = target_columns
        self_.target_dataset = target_dataset
        self_.type = type
