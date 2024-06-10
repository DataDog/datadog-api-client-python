# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.synthetics_assertion_body_hash_operator import SyntheticsAssertionBodyHashOperator
    from datadog_api_client.v1.model.synthetics_assertion_body_hash_type import SyntheticsAssertionBodyHashType


class SyntheticsAssertionBodyHashTarget(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_assertion_body_hash_operator import (
            SyntheticsAssertionBodyHashOperator,
        )
        from datadog_api_client.v1.model.synthetics_assertion_body_hash_type import SyntheticsAssertionBodyHashType

        return {
            "operator": (SyntheticsAssertionBodyHashOperator,),
            "target": (
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
            ),
            "type": (SyntheticsAssertionBodyHashType,),
        }

    attribute_map = {
        "operator": "operator",
        "target": "target",
        "type": "type",
    }

    def __init__(
        self_,
        operator: SyntheticsAssertionBodyHashOperator,
        target: Any,
        type: SyntheticsAssertionBodyHashType,
        **kwargs,
    ):
        """
        An assertion which targets body hash.

        :param operator: Assertion operator to apply.
        :type operator: SyntheticsAssertionBodyHashOperator

        :param target: Value used by the operator.
        :type target: bool, date, datetime, dict, float, int, list, str, UUID, none_type

        :param type: Type of the assertion.
        :type type: SyntheticsAssertionBodyHashType
        """
        super().__init__(kwargs)

        self_.operator = operator
        self_.target = target
        self_.type = type
