# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CreateAppsDatastoreRequestDataAttributesOrgAccess(ModelSimple):
    """
    The organization access level for the datastore. For example, 'contributor'.

    :param value: Must be one of ["contributor", "viewer", "manager"].
    :type value: str
    """

    allowed_values = {
        "contributor",
        "viewer",
        "manager",
    }
    CONTRIBUTOR: ClassVar["CreateAppsDatastoreRequestDataAttributesOrgAccess"]
    VIEWER: ClassVar["CreateAppsDatastoreRequestDataAttributesOrgAccess"]
    MANAGER: ClassVar["CreateAppsDatastoreRequestDataAttributesOrgAccess"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CreateAppsDatastoreRequestDataAttributesOrgAccess.CONTRIBUTOR = CreateAppsDatastoreRequestDataAttributesOrgAccess(
    "contributor"
)
CreateAppsDatastoreRequestDataAttributesOrgAccess.VIEWER = CreateAppsDatastoreRequestDataAttributesOrgAccess("viewer")
CreateAppsDatastoreRequestDataAttributesOrgAccess.MANAGER = CreateAppsDatastoreRequestDataAttributesOrgAccess("manager")
