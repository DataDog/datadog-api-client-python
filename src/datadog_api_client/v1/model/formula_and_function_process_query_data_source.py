# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class FormulaAndFunctionProcessQueryDataSource(StringEnum):
    """
    Data sources that rely on the process backend.

    :param value: Must be one of ["process", "container"].
    :type value: str
    """

    allowed_values = {
        "process",
        "container",
    }
    PROCESS: ClassVar["FormulaAndFunctionProcessQueryDataSource"]
    CONTAINER: ClassVar["FormulaAndFunctionProcessQueryDataSource"]


FormulaAndFunctionProcessQueryDataSource.PROCESS = FormulaAndFunctionProcessQueryDataSource("process")
FormulaAndFunctionProcessQueryDataSource.CONTAINER = FormulaAndFunctionProcessQueryDataSource("container")
