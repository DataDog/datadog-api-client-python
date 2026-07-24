# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class PostmortemTemplateLocation(ModelSimple):
    """
    The location where the postmortem is created and stored.

    :param value: If omitted defaults to "datadog_notebooks". Must be one of ["datadog_notebooks", "confluence", "google_docs"].
    :type value: str
    """

    allowed_values = {
        "datadog_notebooks",
        "confluence",
        "google_docs",
    }
    DATADOG_NOTEBOOKS: ClassVar["PostmortemTemplateLocation"]
    CONFLUENCE: ClassVar["PostmortemTemplateLocation"]
    GOOGLE_DOCS: ClassVar["PostmortemTemplateLocation"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


PostmortemTemplateLocation.DATADOG_NOTEBOOKS = PostmortemTemplateLocation("datadog_notebooks")
PostmortemTemplateLocation.CONFLUENCE = PostmortemTemplateLocation("confluence")
PostmortemTemplateLocation.GOOGLE_DOCS = PostmortemTemplateLocation("google_docs")
