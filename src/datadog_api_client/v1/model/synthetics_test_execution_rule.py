# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class SyntheticsTestExecutionRule(ModelSimple):
    """
    Execution rule for a Synthetics test.

    :param value: Must be one of ["blocking", "non_blocking", "skipped"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "BLOCKING": "blocking",
            "NON_BLOCKING": "non_blocking",
            "SKIPPED": "skipped",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
