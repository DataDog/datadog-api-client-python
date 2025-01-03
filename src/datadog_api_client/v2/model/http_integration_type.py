# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class HTTPIntegrationType(ModelSimple):
    """
    The definition of `HTTPIntegrationType` object.

    :param value: If omitted defaults to "HTTP". Must be one of ["HTTP"].
    :type value: str
    """

    allowed_values = {
        "HTTP",
    }
    HTTP: ClassVar["HTTPIntegrationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


HTTPIntegrationType.HTTP = HTTPIntegrationType("HTTP")
