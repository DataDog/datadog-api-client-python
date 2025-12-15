# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsSuiteTypes(ModelSimple):
    """
    Type for the Synthetics suites responses, `suites`.

    :param value: If omitted defaults to "suites". Must be one of ["suites"].
    :type value: str
    """

    allowed_values = {
        "suites",
    }
    SUITES: ClassVar["SyntheticsSuiteTypes"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsSuiteTypes.SUITES = SyntheticsSuiteTypes("suites")
