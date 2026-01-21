# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class HamrOrgConnectionType(ModelSimple):
    """
    Type of the HAMR organization connection resource.

    :param value: If omitted defaults to "hamr_org_connections". Must be one of ["hamr_org_connections"].
    :type value: str
    """

    allowed_values = {
        "hamr_org_connections",
    }
    HAMR_ORG_CONNECTIONS: ClassVar["HamrOrgConnectionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


HamrOrgConnectionType.HAMR_ORG_CONNECTIONS = HamrOrgConnectionType("hamr_org_connections")
