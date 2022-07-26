# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class SLOCorrectionCategory(ModelSimple):
    """
    Category the SLO correction belongs to.

    :param value: Must be one of ["Scheduled Maintenance", "Outside Business Hours", "Deployment", "Other"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "SCHEDULED_MAINTENANCE": "Scheduled Maintenance",
            "OUTSIDE_BUSINESS_HOURS": "Outside Business Hours",
            "DEPLOYMENT": "Deployment",
            "OTHER": "Other",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
