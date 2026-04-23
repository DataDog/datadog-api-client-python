# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class SyntheticsTestResultAssertionResult(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "actual": (
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
            "error_message": (str,),
            "expected": (
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
            "operator": (str,),
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
                UUID,
                none_type,
            ),
            "target_path": (str,),
            "target_path_operator": (str,),
            "type": (str,),
            "valid": (bool,),
        }

    attribute_map = {
        "actual": "actual",
        "error_message": "error_message",
        "expected": "expected",
        "operator": "operator",
        "_property": "property",
        "target": "target",
        "target_path": "target_path",
        "target_path_operator": "target_path_operator",
        "type": "type",
        "valid": "valid",
    }

    def __init__(
        self_,
        actual: Union[Any, UnsetType] = unset,
        error_message: Union[str, UnsetType] = unset,
        expected: Union[Any, UnsetType] = unset,
        operator: Union[str, UnsetType] = unset,
        _property: Union[str, UnsetType] = unset,
        target: Union[Any, UnsetType] = unset,
        target_path: Union[str, UnsetType] = unset,
        target_path_operator: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        valid: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        An individual assertion result from a Synthetic test.

        :param actual: Actual value observed during the test. Its type depends on the assertion type.
        :type actual: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param error_message: Error message if the assertion failed.
        :type error_message: str, optional

        :param expected: Expected value for the assertion. Its type depends on the assertion type.
        :type expected: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param operator: Operator used for the assertion (for example, ``is`` , ``contains`` ).
        :type operator: str, optional

        :param _property: Property targeted by the assertion, when applicable.
        :type _property: str, optional

        :param target: Target value for the assertion. Its type depends on the assertion type.
        :type target: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param target_path: JSON path or XPath evaluated for the assertion.
        :type target_path: str, optional

        :param target_path_operator: Operator used for the target path assertion.
        :type target_path_operator: str, optional

        :param type: Type of the assertion (for example, ``responseTime`` , ``statusCode`` , ``body`` ).
        :type type: str, optional

        :param valid: Whether the assertion passed.
        :type valid: bool, optional
        """
        if actual is not unset:
            kwargs["actual"] = actual
        if error_message is not unset:
            kwargs["error_message"] = error_message
        if expected is not unset:
            kwargs["expected"] = expected
        if operator is not unset:
            kwargs["operator"] = operator
        if _property is not unset:
            kwargs["_property"] = _property
        if target is not unset:
            kwargs["target"] = target
        if target_path is not unset:
            kwargs["target_path"] = target_path
        if target_path_operator is not unset:
            kwargs["target_path_operator"] = target_path_operator
        if type is not unset:
            kwargs["type"] = type
        if valid is not unset:
            kwargs["valid"] = valid
        super().__init__(kwargs)
