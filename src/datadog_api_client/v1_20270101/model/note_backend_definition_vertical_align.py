# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class NoteBackendDefinitionVerticalAlign(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["center", "top", "bottom"].
    :type value: str
    """

    allowed_values = {
        "center",
        "top",
        "bottom",
    }
    CENTER: ClassVar["NoteBackendDefinitionVerticalAlign"]
    TOP: ClassVar["NoteBackendDefinitionVerticalAlign"]
    BOTTOM: ClassVar["NoteBackendDefinitionVerticalAlign"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


NoteBackendDefinitionVerticalAlign.CENTER = NoteBackendDefinitionVerticalAlign("center")
NoteBackendDefinitionVerticalAlign.TOP = NoteBackendDefinitionVerticalAlign("top")
NoteBackendDefinitionVerticalAlign.BOTTOM = NoteBackendDefinitionVerticalAlign("bottom")
