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


class SyntheticsTestResultStepAssertionResult(ModelNormal):
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
            "check_type": (str,),
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
            "has_secure_variables": (bool,),
        }

    attribute_map = {
        "actual": "actual",
        "check_type": "check_type",
        "expected": "expected",
        "has_secure_variables": "has_secure_variables",
    }

    def __init__(
        self_,
        actual: Union[Any, UnsetType] = unset,
        check_type: Union[str, UnsetType] = unset,
        expected: Union[Any, UnsetType] = unset,
        has_secure_variables: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Assertion result for a browser or mobile step.

        :param actual: Actual value observed during the step assertion. Its type depends on the check type.
        :type actual: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param check_type: Type of the step assertion check.
        :type check_type: str, optional

        :param expected: Expected value for the step assertion. Its type depends on the check type.
        :type expected: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param has_secure_variables: Whether the assertion involves secure variables.
        :type has_secure_variables: bool, optional
        """
        if actual is not unset:
            kwargs["actual"] = actual
        if check_type is not unset:
            kwargs["check_type"] = check_type
        if expected is not unset:
            kwargs["expected"] = expected
        if has_secure_variables is not unset:
            kwargs["has_secure_variables"] = has_secure_variables
        super().__init__(kwargs)
