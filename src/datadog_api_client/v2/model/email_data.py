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
    from datadog_api_client.v2.model.email_attributes import EmailAttributes
    from datadog_api_client.v2.model.email_type import EmailType


class EmailData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.email_attributes import EmailAttributes
        from datadog_api_client.v2.model.email_type import EmailType

        return {
            "attributes": (EmailAttributes,),
            "id": (str,),
            "type": (EmailType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: EmailType,
        attributes: Union[EmailAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data for an on-call email resource.

        :param attributes: Attributes for an on-call email.
        :type attributes: EmailAttributes, optional

        :param id: The email's unique identifier.
        :type id: str, optional

        :param type: Indicates that the resource is of type 'emails'.
        :type type: EmailType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
