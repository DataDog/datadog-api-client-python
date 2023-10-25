# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AWSEventBridgeCreateStatus(ModelSimple):
    """
    The event source status "created".

    :param value: If omitted defaults to "created". Must be one of ["created"].
    :type value: str
    """

    allowed_values = {
        "created",
    }
    CREATED: ClassVar["AWSEventBridgeCreateStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AWSEventBridgeCreateStatus.CREATED = AWSEventBridgeCreateStatus("created")
