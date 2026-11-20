# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class NoteBackendDefinitionTickEdge(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["left", "right", "top", "bottom"].
    :type value: str
    """

    allowed_values = {
        "left",
        "right",
        "top",
        "bottom",
    }
    LEFT: ClassVar["NoteBackendDefinitionTickEdge"]
    RIGHT: ClassVar["NoteBackendDefinitionTickEdge"]
    TOP: ClassVar["NoteBackendDefinitionTickEdge"]
    BOTTOM: ClassVar["NoteBackendDefinitionTickEdge"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


NoteBackendDefinitionTickEdge.LEFT = NoteBackendDefinitionTickEdge("left")
NoteBackendDefinitionTickEdge.RIGHT = NoteBackendDefinitionTickEdge("right")
NoteBackendDefinitionTickEdge.TOP = NoteBackendDefinitionTickEdge("top")
NoteBackendDefinitionTickEdge.BOTTOM = NoteBackendDefinitionTickEdge("bottom")
