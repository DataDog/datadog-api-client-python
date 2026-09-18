# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FormVersionListType(ModelSimple):
    """
    The resource type for a list of form versions.

    :param value: If omitted defaults to "form_version_lists". Must be one of ["form_version_lists"].
    :type value: str
    """

    allowed_values = {
        "form_version_lists",
    }
    FORM_VERSION_LISTS: ClassVar["FormVersionListType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FormVersionListType.FORM_VERSION_LISTS = FormVersionListType("form_version_lists")
