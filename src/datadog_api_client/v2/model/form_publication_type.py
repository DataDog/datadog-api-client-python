# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FormPublicationType(ModelSimple):
    """
    Type for form publications.

    :param value: If omitted defaults to "form_publications". Must be one of ["form_publications"].
    :type value: str
    """

    allowed_values = {
        "form_publications",
    }
    FORM_PUBLICATIONS: ClassVar["FormPublicationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FormPublicationType.FORM_PUBLICATIONS = FormPublicationType("form_publications")
