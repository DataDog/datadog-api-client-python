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


class GoogleChatOrganizationAttributes(ModelNormal):
    validations = {
        "domain_id": {
            "max_length": 255,
        },
        "domain_name": {
            "max_length": 255,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "domain_id": (str,),
            "domain_name": (str,),
        }

    attribute_map = {
        "domain_id": "domain_id",
        "domain_name": "domain_name",
    }

    def __init__(self_, domain_id: Union[str, UnsetType] = unset, domain_name: Union[str, UnsetType] = unset, **kwargs):
        """
        Google Chat organization attributes.

        :param domain_id: The Google Chat organization domain ID.
        :type domain_id: str, optional

        :param domain_name: The Google Chat organization domain name.
        :type domain_name: str, optional
        """
        if domain_id is not unset:
            kwargs["domain_id"] = domain_id
        if domain_name is not unset:
            kwargs["domain_name"] = domain_name
        super().__init__(kwargs)
