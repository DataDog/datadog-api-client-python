# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.synthetics_assertion_operator import SyntheticsAssertionOperator
    from datadog_api_client.v1.model.synthetics_assertion_target_value import SyntheticsAssertionTargetValue
    from datadog_api_client.v1.model.synthetics_assertion_timings_scope import SyntheticsAssertionTimingsScope
    from datadog_api_client.v1.model.synthetics_assertion_type import SyntheticsAssertionType


class SyntheticsAssertionTarget(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_assertion_operator import SyntheticsAssertionOperator
        from datadog_api_client.v1.model.synthetics_assertion_target_value import SyntheticsAssertionTargetValue
        from datadog_api_client.v1.model.synthetics_assertion_timings_scope import SyntheticsAssertionTimingsScope
        from datadog_api_client.v1.model.synthetics_assertion_type import SyntheticsAssertionType

        return {
            "operator": (SyntheticsAssertionOperator,),
            "_property": (str,),
            "target": (SyntheticsAssertionTargetValue,),
            "timings_scope": (SyntheticsAssertionTimingsScope,),
            "type": (SyntheticsAssertionType,),
        }

    attribute_map = {
        "operator": "operator",
        "_property": "property",
        "target": "target",
        "timings_scope": "timingsScope",
        "type": "type",
    }

    def __init__(
        self_,
        operator: SyntheticsAssertionOperator,
        target: Union[SyntheticsAssertionTargetValue, float, str],
        type: SyntheticsAssertionType,
        _property: Union[str, UnsetType] = unset,
        timings_scope: Union[SyntheticsAssertionTimingsScope, UnsetType] = unset,
        **kwargs,
    ):
        """
        An assertion which uses a simple target.

        :param operator: Assertion operator to apply.
        :type operator: SyntheticsAssertionOperator

        :param _property: The associated assertion property.
        :type _property: str, optional

        :param target: Value used by the operator in assertions. Can be either a number or string.
        :type target: SyntheticsAssertionTargetValue

        :param timings_scope: Timings scope for response time assertions.
        :type timings_scope: SyntheticsAssertionTimingsScope, optional

        :param type: Type of the assertion.
        :type type: SyntheticsAssertionType
        """
        if _property is not unset:
            kwargs["_property"] = _property
        if timings_scope is not unset:
            kwargs["timings_scope"] = timings_scope
        super().__init__(kwargs)

        self_.operator = operator
        self_.target = target
        self_.type = type
