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
    from datadog_api_client.v2.model.spec_attributes_status import SpecAttributesStatus


class SpecAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.spec_attributes_status import SpecAttributesStatus

        return {
            "name": (str,),
            "status": (SpecAttributesStatus,),
            "version": (str,),
        }

    attribute_map = {
        "name": "name",
        "status": "status",
        "version": "version",
    }

    def __init__(
        self_,
        name: Union[str, UnsetType] = unset,
        status: Union[SpecAttributesStatus, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an API spec.

        :param name: The name of the spec.
        :type name: str, optional

        :param status: The publication status of the spec.
        :type status: SpecAttributesStatus, optional

        :param version: The version of the spec.
        :type version: str, optional
        """
        if name is not unset:
            kwargs["name"] = name
        if status is not unset:
            kwargs["status"] = status
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
