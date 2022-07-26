# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class MetricBulkConfigureTagsType(ModelSimple):
    """
    The metric bulk configure tags resource.

    :param value: If omitted defaults to "metric_bulk_configure_tags". Must be one of ["metric_bulk_configure_tags"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "BULK_MANAGE_TAGS": "metric_bulk_configure_tags",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
