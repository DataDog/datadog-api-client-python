# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class LogsArchiveDestinationGCSType(ModelSimple):
    """
    Type of the GCS archive destination.

    :param value: If omitted defaults to "gcs". Must be one of ["gcs"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "GCS": "gcs",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
