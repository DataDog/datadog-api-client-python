# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class CustomerOrgDisableRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "org_uuid": (str,),
        }

    attribute_map = {
        "org_uuid": "org_uuid",
    }

    def __init__(self_, org_uuid: Union[str, UnsetType] = unset, **kwargs):
        """
        Optional attributes for a customer org disable request. When supplied, ``org_uuid``
        must match the authenticated organization or the request is rejected.

        :param org_uuid: Datadog organization UUID. If supplied, must match the authenticated
            organization.
        :type org_uuid: str, optional
        """
        if org_uuid is not unset:
            kwargs["org_uuid"] = org_uuid
        super().__init__(kwargs)
