# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.cohort_scope20270101_target import CohortScope20270101Target
    from datadog_api_client.v1_20270101.model.cohort_scope_type import CohortScopeType
    from datadog_api_client.v1_20270101.model.cohort_scope20270101_target_one_of import CohortScope20270101TargetOneOf
    from datadog_api_client.v1_20270101.model.cohort_scope20270101_target_one_of4454865216 import (
        CohortScope20270101TargetOneOf4454865216,
    )


class CohortScope(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.cohort_scope20270101_target import CohortScope20270101Target
        from datadog_api_client.v1_20270101.model.cohort_scope_type import CohortScopeType

        return {
            "target": (CohortScope20270101Target,),
            "type": (CohortScopeType,),
        }

    attribute_map = {
        "target": "target",
        "type": "type",
    }

    def __init__(
        self_,
        target: Union[
            CohortScope20270101Target, CohortScope20270101TargetOneOf, CohortScope20270101TargetOneOf4454865216
        ],
        type: CohortScopeType,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param target: Test-only generated schema for the dashboard versioning proof of concept.
        :type target: CohortScope20270101Target

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: CohortScopeType
        """
        super().__init__(kwargs)

        self_.target = target
        self_.type = type
