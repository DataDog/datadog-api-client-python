# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class NotebookStatus(ModelSimple):
    """
    Publication status of the notebook. For now, always "published".

    :param value: If omitted defaults to "published". Must be one of ["published"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "PUBLISHED": "published",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
