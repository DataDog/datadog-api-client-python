# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class TeamHierarchyMemberAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "direct_role": (str, none_type),
            "is_direct": (bool,),
            "provisioned_by": (str, none_type),
            "provisioned_by_id": (str, none_type),
        }

    attribute_map = {
        "direct_role": "direct_role",
        "is_direct": "is_direct",
        "provisioned_by": "provisioned_by",
        "provisioned_by_id": "provisioned_by_id",
    }

    def __init__(
        self_,
        direct_role: Union[str, none_type],
        is_direct: bool,
        provisioned_by: Union[str, none_type],
        provisioned_by_id: Union[str, none_type],
        **kwargs,
    ):
        """
        Membership attributes relative to the requested team.

        :param direct_role: Role on the requested team: admin or member. Null for inherited members.
        :type direct_role: str, none_type

        :param is_direct: Whether the user belongs directly to the requested team.
        :type is_direct: bool

        :param provisioned_by: Membership provisioner. Null for inherited members.
        :type provisioned_by: str, none_type

        :param provisioned_by_id: Identifier supplied by the membership provisioner. Null when unavailable or for inherited members.
        :type provisioned_by_id: str, none_type
        """
        super().__init__(kwargs)

        self_.direct_role = direct_role
        self_.is_direct = is_direct
        self_.provisioned_by = provisioned_by
        self_.provisioned_by_id = provisioned_by_id
