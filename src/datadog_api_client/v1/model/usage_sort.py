# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class UsageSort(ModelSimple):
    """
    The field to sort by.

    :param value: If omitted defaults to "start_date". Must be one of ["computed_on", "size", "start_date", "end_date"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "COMPUTED_ON": "computed_on",
            "SIZE": "size",
            "START_DATE": "start_date",
            "END_DATE": "end_date",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
