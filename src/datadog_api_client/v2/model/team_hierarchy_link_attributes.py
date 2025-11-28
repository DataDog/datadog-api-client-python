# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class TeamHierarchyLinkAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "provisioned_by": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "provisioned_by": "provisioned_by",
    }

    def __init__(self_, created_at: datetime, provisioned_by: str, **kwargs):
        """
        Team hierarchy link attributes

        :param created_at: Timestamp when the team hierarchy link was created
        :type created_at: datetime

        :param provisioned_by: The provisioner of the team hierarchy link
        :type provisioned_by: str
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.provisioned_by = provisioned_by
