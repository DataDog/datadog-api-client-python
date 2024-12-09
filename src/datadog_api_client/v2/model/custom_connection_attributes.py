# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.custom_connection_attributes_on_prem_runner import (
        CustomConnectionAttributesOnPremRunner,
    )


class CustomConnectionAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_connection_attributes_on_prem_runner import (
            CustomConnectionAttributesOnPremRunner,
        )

        return {
            "name": (str,),
            "on_prem_runner": (CustomConnectionAttributesOnPremRunner,),
        }

    attribute_map = {
        "name": "name",
        "on_prem_runner": "onPremRunner",
    }

    def __init__(
        self_,
        name: Union[str, UnsetType] = unset,
        on_prem_runner: Union[CustomConnectionAttributesOnPremRunner, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``CustomConnectionAttributes`` object.

        :param name: The ``attributes`` ``name``.
        :type name: str, optional

        :param on_prem_runner: The definition of ``CustomConnectionAttributesOnPremRunner`` object.
        :type on_prem_runner: CustomConnectionAttributesOnPremRunner, optional
        """
        if name is not unset:
            kwargs["name"] = name
        if on_prem_runner is not unset:
            kwargs["on_prem_runner"] = on_prem_runner
        super().__init__(kwargs)
