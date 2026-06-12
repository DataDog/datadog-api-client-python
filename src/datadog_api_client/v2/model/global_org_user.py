# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


class GlobalOrgUser(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "handle": (str,),
            "uuid": (UUID,),
        }

    attribute_map = {
        "handle": "handle",
        "uuid": "uuid",
    }

    def __init__(self_, handle: str, uuid: UUID, **kwargs):
        """
        User information for a global organization association.

        :param handle: The handle of the user.
        :type handle: str

        :param uuid: The UUID of the user.
        :type uuid: UUID
        """
        super().__init__(kwargs)

        self_.handle = handle
        self_.uuid = uuid
