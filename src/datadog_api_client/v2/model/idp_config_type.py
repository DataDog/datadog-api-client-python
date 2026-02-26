# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IDPConfigType(ModelSimple):
    """
    Resource type.

    :param value: If omitted defaults to "idp_config". Must be one of ["idp_config"].
    :type value: str
    """

    allowed_values = {
        "idp_config",
    }
    IDP_CONFIG: ClassVar["IDPConfigType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IDPConfigType.IDP_CONFIG = IDPConfigType("idp_config")
