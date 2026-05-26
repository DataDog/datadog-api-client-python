# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.analysis_violation import AnalysisViolation


class AnalysisRuleResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.analysis_violation import AnalysisViolation

        return {
            "errors": ([str],),
            "execution_error": (str, none_type),
            "execution_time_ms": (int,),
            "identifier": (str,),
            "output": (str,),
            "violations": ([AnalysisViolation],),
        }

    attribute_map = {
        "errors": "errors",
        "execution_error": "execution_error",
        "execution_time_ms": "execution_time_ms",
        "identifier": "identifier",
        "output": "output",
        "violations": "violations",
    }

    def __init__(
        self_,
        errors: List[str],
        execution_error: Union[str, none_type],
        execution_time_ms: int,
        identifier: str,
        output: str,
        violations: List[AnalysisViolation],
        **kwargs,
    ):
        """
        The result of applying a single static analysis rule to the analyzed source code.

        :param errors: A list of error messages encountered while executing the rule.
        :type errors: [str]

        :param execution_error: An error message if the rule execution failed, or null if execution succeeded.
        :type execution_error: str, none_type

        :param execution_time_ms: The time taken to execute the rule, in milliseconds.
        :type execution_time_ms: int

        :param identifier: The identifier of the rule that produced this response.
        :type identifier: str

        :param output: The raw output produced by the rule engine during execution.
        :type output: str

        :param violations: The list of violations found by this rule.
        :type violations: [AnalysisViolation]
        """
        super().__init__(kwargs)

        self_.errors = errors
        self_.execution_error = execution_error
        self_.execution_time_ms = execution_time_ms
        self_.identifier = identifier
        self_.output = output
        self_.violations = violations
