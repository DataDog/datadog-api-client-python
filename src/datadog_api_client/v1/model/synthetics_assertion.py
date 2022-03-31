# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.synthetics_assertion_target import SyntheticsAssertionTarget
    from datadog_api_client.v1.model.synthetics_assertion_json_path_target import SyntheticsAssertionJSONPathTarget

    globals()["SyntheticsAssertionTarget"] = SyntheticsAssertionTarget
    globals()["SyntheticsAssertionJSONPathTarget"] = SyntheticsAssertionJSONPathTarget


class SyntheticsAssertion(ModelComposed):
    def __init__(self, *args, **kwargs):
        """
        Object describing the assertions type, their associated operator,
        which property they apply, and upon which target.

        :param operator: Assertion operator to apply.
        :type operator: SyntheticsAssertionOperator

        :param _property: The associated assertion property.
        :type _property: str, optional

        :param target: Value used by the operator.
        :type target: bool, date, datetime, dict, float, int, list, str, none_type

        :param type: Type of the assertion.
        :type type: SyntheticsAssertionType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsAssertion, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
            "anyOf": [],
            "allOf": [],
            "oneOf": [
                SyntheticsAssertionTarget,
                SyntheticsAssertionJSONPathTarget,
            ],
        }
