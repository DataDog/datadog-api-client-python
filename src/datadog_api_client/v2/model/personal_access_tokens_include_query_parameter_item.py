# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class PersonalAccessTokensIncludeQueryParameterItem(ModelSimple):
    """
    Relationship object that should be included in the response.

    :param value: If omitted defaults to "leak_information". Must be one of ["leak_information"].
    :type value: str
    """

    allowed_values = {
        "leak_information",
    }
    LEAK_INFORMATION: ClassVar["PersonalAccessTokensIncludeQueryParameterItem"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


PersonalAccessTokensIncludeQueryParameterItem.LEAK_INFORMATION = PersonalAccessTokensIncludeQueryParameterItem(
    "leak_information"
)
