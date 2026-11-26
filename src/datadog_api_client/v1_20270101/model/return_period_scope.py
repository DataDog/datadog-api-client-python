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
    from datadog_api_client.v1_20270101.model.return_period_scope_target import ReturnPeriodScopeTarget
    from datadog_api_client.v1_20270101.model.return_period_scope_type import ReturnPeriodScopeType


class ReturnPeriodScope(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.return_period_scope_target import ReturnPeriodScopeTarget
        from datadog_api_client.v1_20270101.model.return_period_scope_type import ReturnPeriodScopeType

        return {
            "target": (ReturnPeriodScopeTarget,),
            "type": (ReturnPeriodScopeType,),
        }

    attribute_map = {
        "target": "target",
        "type": "type",
    }

    def __init__(self_, target: ReturnPeriodScopeTarget, type: ReturnPeriodScopeType, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param target: Test-only generated schema for the dashboard versioning proof of concept.
        :type target: ReturnPeriodScopeTarget

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: ReturnPeriodScopeType
        """
        super().__init__(kwargs)

        self_.target = target
        self_.type = type
