# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FormulaAndFunctionSLOGroupMode(ModelSimple):
    """
    Group mode to query measures.

    :param value: Must be one of ["overall", "components"].
    :type value: str
    """

    allowed_values = {
        "overall",
        "components",
    }
    OVERALL: ClassVar["FormulaAndFunctionSLOGroupMode"]
    COMPONENTS: ClassVar["FormulaAndFunctionSLOGroupMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FormulaAndFunctionSLOGroupMode.OVERALL = FormulaAndFunctionSLOGroupMode("overall")
FormulaAndFunctionSLOGroupMode.COMPONENTS = FormulaAndFunctionSLOGroupMode("components")
