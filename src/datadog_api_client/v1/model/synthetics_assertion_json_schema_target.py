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
    from datadog_api_client.v1.model.synthetics_assertion_json_schema_operator import (
        SyntheticsAssertionJSONSchemaOperator,
    )
    from datadog_api_client.v1.model.synthetics_assertion_json_schema_target_target import (
        SyntheticsAssertionJSONSchemaTargetTarget,
    )
    from datadog_api_client.v1.model.synthetics_assertion_type import SyntheticsAssertionType


class SyntheticsAssertionJSONSchemaTarget(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_assertion_json_schema_operator import (
            SyntheticsAssertionJSONSchemaOperator,
        )
        from datadog_api_client.v1.model.synthetics_assertion_json_schema_target_target import (
            SyntheticsAssertionJSONSchemaTargetTarget,
        )
        from datadog_api_client.v1.model.synthetics_assertion_type import SyntheticsAssertionType

        return {
            "operator": (SyntheticsAssertionJSONSchemaOperator,),
            "target": (SyntheticsAssertionJSONSchemaTargetTarget,),
            "type": (SyntheticsAssertionType,),
        }

    attribute_map = {
        "operator": "operator",
        "target": "target",
        "type": "type",
    }

    def __init__(
        self_,
        operator: SyntheticsAssertionJSONSchemaOperator,
        type: SyntheticsAssertionType,
        target: Union[SyntheticsAssertionJSONSchemaTargetTarget, UnsetType] = unset,
        **kwargs,
    ):
        """
        An assertion for the ``validatesJSONSchema`` operator.

        :param operator: Assertion operator to apply.
        :type operator: SyntheticsAssertionJSONSchemaOperator

        :param target: Composed target for ``validatesJSONSchema`` operator.
        :type target: SyntheticsAssertionJSONSchemaTargetTarget, optional

        :param type: Type of the assertion.
        :type type: SyntheticsAssertionType
        """
        if target is not unset:
            kwargs["target"] = target
        super().__init__(kwargs)

        self_.operator = operator
        self_.type = type
