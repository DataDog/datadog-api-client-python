# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IntegrationAssignmentDataAttributesRequestAction(ModelSimple):
    """
    Action to perform on the assignment. Can be "assign" or "un_assign".

    :param value: Must be one of ["assign", "un_assign"].
    :type value: str
    """

    allowed_values = {
        "assign",
        "un_assign",
    }
    ASSIGN: ClassVar["IntegrationAssignmentDataAttributesRequestAction"]
    UN_ASSIGN: ClassVar["IntegrationAssignmentDataAttributesRequestAction"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IntegrationAssignmentDataAttributesRequestAction.ASSIGN = IntegrationAssignmentDataAttributesRequestAction("assign")
IntegrationAssignmentDataAttributesRequestAction.UN_ASSIGN = IntegrationAssignmentDataAttributesRequestAction(
    "un_assign"
)
