# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class SyntheticsTestProcessStatus(ModelSimple):
    """
    Status of a Synthetic test.

    :param value: Must be one of ["not_scheduled", "scheduled", "finished", "finished_with_error"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "NOT_SCHEDULED": "not_scheduled",
            "SCHEDULED": "scheduled",
            "FINISHED": "finished",
            "FINISHED_WITH_ERROR": "finished_with_error",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
