# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


class OrgGroupPolicyOverrideUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "org_site": (str,),
            "org_uuid": (UUID,),
        }

    attribute_map = {
        "org_site": "org_site",
        "org_uuid": "org_uuid",
    }

    def __init__(self_, org_site: str, org_uuid: UUID, **kwargs):
        """
        Attributes for updating a policy override. The ``org_uuid`` and ``org_site`` fields must match the existing override and cannot be changed.

        :param org_site: The site of the organization.
        :type org_site: str

        :param org_uuid: The UUID of the organization.
        :type org_uuid: UUID
        """
        super().__init__(kwargs)

        self_.org_site = org_site
        self_.org_uuid = org_uuid
