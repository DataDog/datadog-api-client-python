# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DashboardSearchUser(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "handle": (str,),
            "name": (str,),
        }

    attribute_map = {
        "handle": "handle",
        "name": "name",
    }

    def __init__(self_, handle: str, name: str, **kwargs):
        """
        User information.

        :param handle: User handle or email.
        :type handle: str

        :param name: User display name.
        :type name: str
        """
        super().__init__(kwargs)

        self_.handle = handle
        self_.name = name
