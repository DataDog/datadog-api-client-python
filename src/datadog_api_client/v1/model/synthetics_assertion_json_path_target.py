# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsAssertionJSONPathTarget(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_assertion_json_path_operator import (
            SyntheticsAssertionJSONPathOperator,
        )
        from datadog_api_client.v1.model.synthetics_assertion_json_path_target_target import (
            SyntheticsAssertionJSONPathTargetTarget,
        )
        from datadog_api_client.v1.model.synthetics_assertion_type import SyntheticsAssertionType

        return {
            "operator": (SyntheticsAssertionJSONPathOperator,),
            "_property": (str,),
            "target": (SyntheticsAssertionJSONPathTargetTarget,),
            "type": (SyntheticsAssertionType,),
        }

    attribute_map = {
        "operator": "operator",
        "_property": "property",
        "target": "target",
        "type": "type",
    }

    def __init__(self, operator, type, *args, **kwargs):
        """
        An assertion for the ``validatesJSONPath`` operator.

        :param operator: Assertion operator to apply.
        :type operator: SyntheticsAssertionJSONPathOperator

        :param _property: The associated assertion property.
        :type _property: str, optional

        :param target: Composed target for ``validatesJSONPath`` operator.
        :type target: SyntheticsAssertionJSONPathTargetTarget, optional

        :param type: Type of the assertion.
        :type type: SyntheticsAssertionType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.operator = operator
        self.type = type

    @classmethod
    def _from_openapi_data(cls, operator, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsAssertionJSONPathTarget, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.operator = operator
        self.type = type
        return self
