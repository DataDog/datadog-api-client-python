# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class StatusPagesComponentGroupAttributesComponentsItemsStatus(ModelSimple):
    """
    The status of the component.

    :param value: Must be one of ["operational", "degraded", "partial_outage", "major_outage"].
    :type value: str
    """

    allowed_values = {
        "operational",
        "degraded",
        "partial_outage",
        "major_outage",
    }
    OPERATIONAL: ClassVar["StatusPagesComponentGroupAttributesComponentsItemsStatus"]
    DEGRADED: ClassVar["StatusPagesComponentGroupAttributesComponentsItemsStatus"]
    PARTIAL_OUTAGE: ClassVar["StatusPagesComponentGroupAttributesComponentsItemsStatus"]
    MAJOR_OUTAGE: ClassVar["StatusPagesComponentGroupAttributesComponentsItemsStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


StatusPagesComponentGroupAttributesComponentsItemsStatus.OPERATIONAL = (
    StatusPagesComponentGroupAttributesComponentsItemsStatus("operational")
)
StatusPagesComponentGroupAttributesComponentsItemsStatus.DEGRADED = (
    StatusPagesComponentGroupAttributesComponentsItemsStatus("degraded")
)
StatusPagesComponentGroupAttributesComponentsItemsStatus.PARTIAL_OUTAGE = (
    StatusPagesComponentGroupAttributesComponentsItemsStatus("partial_outage")
)
StatusPagesComponentGroupAttributesComponentsItemsStatus.MAJOR_OUTAGE = (
    StatusPagesComponentGroupAttributesComponentsItemsStatus("major_outage")
)
