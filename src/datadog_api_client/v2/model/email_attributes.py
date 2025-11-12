# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.email_format_type import EmailFormatType


class EmailAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.email_format_type import EmailFormatType

        return {
            "active": (bool,),
            "address": (str,),
            "alias": (str,),
            "formats": ([EmailFormatType],),
        }

    attribute_map = {
        "active": "active",
        "address": "address",
        "alias": "alias",
        "formats": "formats",
    }

    def __init__(
        self_,
        active: Union[bool, UnsetType] = unset,
        address: Union[str, UnsetType] = unset,
        alias: Union[str, UnsetType] = unset,
        formats: Union[List[EmailFormatType], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for an on-call email.

        :param active: Whether the email is currently active.
        :type active: bool, optional

        :param address: Email address.
        :type address: str, optional

        :param alias: Optional display alias for the email.
        :type alias: str, optional

        :param formats: Preferred content formats for notifications.
        :type formats: [EmailFormatType], optional
        """
        if active is not unset:
            kwargs["active"] = active
        if address is not unset:
            kwargs["address"] = address
        if alias is not unset:
            kwargs["alias"] = alias
        if formats is not unset:
            kwargs["formats"] = formats
        super().__init__(kwargs)
