# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.global_org import GlobalOrg
    from datadog_api_client.v2.model.global_org_user import GlobalOrgUser


class GlobalOrgAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.global_org import GlobalOrg
        from datadog_api_client.v2.model.global_org_user import GlobalOrgUser

        return {
            "org": (GlobalOrg,),
            "redirect_url": (str, none_type),
            "source_region": (str,),
            "user": (GlobalOrgUser,),
        }

    attribute_map = {
        "org": "org",
        "redirect_url": "redirect_url",
        "source_region": "source_region",
        "user": "user",
    }

    def __init__(
        self_,
        org: GlobalOrg,
        source_region: str,
        user: GlobalOrgUser,
        redirect_url: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an organization associated with the authenticated user.

        :param org: Organization information for a global organization association.
        :type org: GlobalOrg

        :param redirect_url: The login URL used to switch into the organization, if available.
        :type redirect_url: str, none_type, optional

        :param source_region: The source region of the organization.
        :type source_region: str

        :param user: User information for a global organization association.
        :type user: GlobalOrgUser
        """
        if redirect_url is not unset:
            kwargs["redirect_url"] = redirect_url
        super().__init__(kwargs)

        self_.org = org
        self_.source_region = source_region
        self_.user = user
