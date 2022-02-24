# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
)


def lazy_import():
    from datadog_api_client.v1.model.synthetics_assertion_operator import SyntheticsAssertionOperator
    from datadog_api_client.v1.model.synthetics_assertion_type import SyntheticsAssertionType

    globals()["SyntheticsAssertionOperator"] = SyntheticsAssertionOperator
    globals()["SyntheticsAssertionType"] = SyntheticsAssertionType


class SyntheticsAssertionTarget(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "operator": (SyntheticsAssertionOperator,),
            "_property": (str,),
            "target": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                none_type,
            ),
            "type": (SyntheticsAssertionType,),
        }

    attribute_map = {
        "operator": "operator",
        "_property": "property",
        "target": "target",
        "type": "type",
    }

    read_only_vars = {}

    def __init__(self, operator, target, type, *args, **kwargs):
        """
        An assertion which uses a simple target.

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

        self.operator = operator
        self.target = target
        self.type = type

    @classmethod
    def _from_openapi_data(cls, operator, target, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsAssertionTarget, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.operator = operator
        self.target = target
        self.type = type
        return self
