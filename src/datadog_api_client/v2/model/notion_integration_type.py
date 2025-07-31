# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class NotionIntegrationType(ModelSimple):
    """
    The definition of the `NotionIntegrationType` object.

    :param value: If omitted defaults to "Notion". Must be one of ["Notion"].
    :type value: str
    """

    allowed_values = {
        "Notion",
    }
    NOTION: ClassVar["NotionIntegrationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


NotionIntegrationType.NOTION = NotionIntegrationType("Notion")
