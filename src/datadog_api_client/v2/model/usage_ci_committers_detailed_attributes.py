# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class UsageCICommittersDetailedAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "org_name": (str,),
            "public_id": (str,),
            "region": (str,),
            "timestamp": (datetime,),
            "usage_type": (str,),
            "user_email": (str,),
        }

    attribute_map = {
        "org_name": "org_name",
        "public_id": "public_id",
        "region": "region",
        "timestamp": "timestamp",
        "usage_type": "usage_type",
        "user_email": "user_email",
    }

    def __init__(
        self_,
        org_name: Union[str, UnsetType] = unset,
        public_id: Union[str, UnsetType] = unset,
        region: Union[str, UnsetType] = unset,
        timestamp: Union[datetime, UnsetType] = unset,
        usage_type: Union[str, UnsetType] = unset,
        user_email: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The response containing CI Committers Detailed attributes for specified organization.

        :param org_name: The organization name.
        :type org_name: str, optional

        :param public_id: The organization public ID.
        :type public_id: str, optional

        :param region: The region of the organization.
        :type region: str, optional

        :param timestamp: Shows the hour of the usage.
        :type timestamp: datetime, optional

        :param usage_type: The usage type associated with the commit.
        :type usage_type: str, optional

        :param user_email: The user email of CI committer.
        :type user_email: str, optional
        """
        if org_name is not unset:
            kwargs["org_name"] = org_name
        if public_id is not unset:
            kwargs["public_id"] = public_id
        if region is not unset:
            kwargs["region"] = region
        if timestamp is not unset:
            kwargs["timestamp"] = timestamp
        if usage_type is not unset:
            kwargs["usage_type"] = usage_type
        if user_email is not unset:
            kwargs["user_email"] = user_email
        super().__init__(kwargs)
