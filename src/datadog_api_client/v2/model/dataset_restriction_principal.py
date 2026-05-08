# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DatasetRestrictionPrincipal(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (str,),
            "name": (str,),
            "type": (str,),
        }

    attribute_map = {
        "id": "id",
        "name": "name",
        "type": "type",
    }

    def __init__(self_, id: str, name: str, type: str, **kwargs):
        """
        A user or role that is exempt from dataset restrictions and retains unrestricted
        access to all datasets for the product type.

        :param id: The unique identifier of the principal (a user UUID or role ID).
        :type id: str

        :param name: The human-readable display name of the principal as shown in the Datadog UI.
        :type name: str

        :param type: The kind of principal, such as ``user`` for an individual user account or ``role``
            for a Datadog role.
        :type type: str
        """
        super().__init__(kwargs)

        self_.id = id
        self_.name = name
        self_.type = type
