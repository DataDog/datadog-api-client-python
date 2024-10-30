# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.domain_allowlist_attributes import DomainAllowlistAttributes
    from datadog_api_client.v2.model.domain_allowlist_type import DomainAllowlistType


class DomainAllowlist(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.domain_allowlist_attributes import DomainAllowlistAttributes
        from datadog_api_client.v2.model.domain_allowlist_type import DomainAllowlistType

        return {
            "attributes": (DomainAllowlistAttributes,),
            "id": (str, none_type),
            "type": (DomainAllowlistType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: DomainAllowlistType,
        attributes: Union[DomainAllowlistAttributes, UnsetType] = unset,
        id: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        The email domain allowlist for an org.

        :param attributes: The details of the email domain allowlist.
        :type attributes: DomainAllowlistAttributes, optional

        :param id: The unique identifier of the org.
        :type id: str, none_type, optional

        :param type: Email domain allowlist allowlist type.
        :type type: DomainAllowlistType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
