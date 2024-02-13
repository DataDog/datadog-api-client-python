# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CaseSortableField(ModelSimple):
    """
    Case field that can be sorted on

    :param value: Must be one of ["created_at", "priority", "status"].
    :type value: str
    """

    allowed_values = {
        "created_at",
        "priority",
        "status",
    }
    CREATED_AT: ClassVar["CaseSortableField"]
    PRIORITY: ClassVar["CaseSortableField"]
    STATUS: ClassVar["CaseSortableField"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CaseSortableField.CREATED_AT = CaseSortableField("created_at")
CaseSortableField.PRIORITY = CaseSortableField("priority")
CaseSortableField.STATUS = CaseSortableField("status")
