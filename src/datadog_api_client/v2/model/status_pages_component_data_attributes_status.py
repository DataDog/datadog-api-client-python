# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class StatusPagesComponentDataAttributesStatus(ModelSimple):
    """


    :param value: Must be one of ["operational", "degraded", "partial_outage", "major_outage"].
    :type value: str
    """

    allowed_values = {
        "operational",
        "degraded",
        "partial_outage",
        "major_outage",
    }
    OPERATIONAL: ClassVar["StatusPagesComponentDataAttributesStatus"]
    DEGRADED: ClassVar["StatusPagesComponentDataAttributesStatus"]
    PARTIAL_OUTAGE: ClassVar["StatusPagesComponentDataAttributesStatus"]
    MAJOR_OUTAGE: ClassVar["StatusPagesComponentDataAttributesStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


StatusPagesComponentDataAttributesStatus.OPERATIONAL = StatusPagesComponentDataAttributesStatus("operational")
StatusPagesComponentDataAttributesStatus.DEGRADED = StatusPagesComponentDataAttributesStatus("degraded")
StatusPagesComponentDataAttributesStatus.PARTIAL_OUTAGE = StatusPagesComponentDataAttributesStatus("partial_outage")
StatusPagesComponentDataAttributesStatus.MAJOR_OUTAGE = StatusPagesComponentDataAttributesStatus("major_outage")
