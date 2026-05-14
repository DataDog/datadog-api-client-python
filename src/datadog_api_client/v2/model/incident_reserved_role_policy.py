# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentReservedRolePolicy(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "is_single": (bool,),
        }

    attribute_map = {
        "is_single": "is_single",
    }

    def __init__(self_, is_single: bool, **kwargs):
        """
        Policy for a reserved role.

        :param is_single: Whether this role can only be assigned to a single responder.
        :type is_single: bool
        """
        super().__init__(kwargs)

        self_.is_single = is_single
