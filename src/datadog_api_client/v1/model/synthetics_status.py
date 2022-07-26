# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class SyntheticsStatus(ModelSimple):
    """
    Determines whether or not the batch has passed, failed, or is in progress.

    :param value: Must be one of ["passed", "skipped", "failed"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "PASSED": "passed",
            "skipped": "skipped",
            "failed": "failed",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
