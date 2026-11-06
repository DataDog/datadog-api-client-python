# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OIDCCloudAuthOrgUUIDSource(ModelSimple):
    """
    Source of the organization UUID in the signed token. The `aud` source accepts a datadog/{org_uuid} audience.

    :param value: If omitted defaults to "dd_org_uuid". Must be one of ["dd_org_uuid", "aud"].
    :type value: str
    """

    allowed_values = {
        "dd_org_uuid",
        "aud",
    }
    DD_ORG_UUID: ClassVar["OIDCCloudAuthOrgUUIDSource"]
    AUD: ClassVar["OIDCCloudAuthOrgUUIDSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OIDCCloudAuthOrgUUIDSource.DD_ORG_UUID = OIDCCloudAuthOrgUUIDSource("dd_org_uuid")
OIDCCloudAuthOrgUUIDSource.AUD = OIDCCloudAuthOrgUUIDSource("aud")
