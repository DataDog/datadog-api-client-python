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


class OrgAuthorizedClientUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "disabled": (bool,),
        }

    attribute_map = {
        "disabled": "disabled",
    }

    def __init__(self_, disabled: Union[bool, UnsetType] = unset, **kwargs):
        """
        Attributes for updating an org authorized client.

        :param disabled: Whether to disable or enable this client for the organization.
        :type disabled: bool, optional
        """
        if disabled is not unset:
            kwargs["disabled"] = disabled
        super().__init__(kwargs)
