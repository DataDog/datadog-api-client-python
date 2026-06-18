# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class VercelEnvironment(ModelSimple):
    """
    Vercel deployment environment.

    :param value: Must be one of ["production", "preview"].
    :type value: str
    """

    allowed_values = {
        "production",
        "preview",
    }
    PRODUCTION: ClassVar["VercelEnvironment"]
    PREVIEW: ClassVar["VercelEnvironment"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


VercelEnvironment.PRODUCTION = VercelEnvironment("production")
VercelEnvironment.PREVIEW = VercelEnvironment("preview")
