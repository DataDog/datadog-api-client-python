# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OCIConfigType(ModelSimple):
    """
    Type of OCI config.

    :param value: If omitted defaults to "oci_config". Must be one of ["oci_config"].
    :type value: str
    """

    allowed_values = {
        "oci_config",
    }
    OCI_CONFIG: ClassVar["OCIConfigType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OCIConfigType.OCI_CONFIG = OCIConfigType("oci_config")
