# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ChangeRequestIncludedUserAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "email": (str,),
            "handle": (str,),
            "name": (str,),
        }

    attribute_map = {
        "email": "email",
        "handle": "handle",
        "name": "name",
    }

    def __init__(self_, email: str, handle: str, name: str, **kwargs):
        """
        Attributes of an included user.

        :param email: The email of the user.
        :type email: str

        :param handle: The handle of the user.
        :type handle: str

        :param name: The name of the user.
        :type name: str
        """
        super().__init__(kwargs)

        self_.email = email
        self_.handle = handle
        self_.name = name
