# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class EntityV3QueueKind(ModelSimple):
    """
    The definition of Entity V3 Queue Kind object.

    :param value: If omitted defaults to "queue". Must be one of ["queue"].
    :type value: str
    """

    allowed_values = {
        "queue",
    }
    QUEUE: ClassVar["EntityV3QueueKind"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EntityV3QueueKind.QUEUE = EntityV3QueueKind("queue")
