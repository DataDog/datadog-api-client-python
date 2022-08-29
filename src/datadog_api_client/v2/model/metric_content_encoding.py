# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class MetricContentEncoding(ModelSimple):
    """
    HTTP header used to compress the media-type.

    :param value: If omitted defaults to "deflate". Must be one of ["deflate", "zstd1", "gzip"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "DEFLATE": "deflate",
            "ZSTD1": "zstd1",
            "GZIP": "gzip",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
