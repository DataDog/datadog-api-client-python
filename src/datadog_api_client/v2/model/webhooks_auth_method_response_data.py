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
    from datadog_api_client.v2.model.webhooks_auth_method_attributes import WebhooksAuthMethodAttributes
    from datadog_api_client.v2.model.webhooks_auth_method_relationships import WebhooksAuthMethodRelationships
    from datadog_api_client.v2.model.webhooks_auth_method_type import WebhooksAuthMethodType


class WebhooksAuthMethodResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.webhooks_auth_method_attributes import WebhooksAuthMethodAttributes
        from datadog_api_client.v2.model.webhooks_auth_method_relationships import WebhooksAuthMethodRelationships
        from datadog_api_client.v2.model.webhooks_auth_method_type import WebhooksAuthMethodType

        return {
            "attributes": (WebhooksAuthMethodAttributes,),
            "id": (str,),
            "relationships": (WebhooksAuthMethodRelationships,),
            "type": (WebhooksAuthMethodType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: WebhooksAuthMethodAttributes,
        id: str,
        type: WebhooksAuthMethodType,
        relationships: Union[WebhooksAuthMethodRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Webhooks auth method data from a response.

        :param attributes: Attributes of a webhooks auth method.
        :type attributes: WebhooksAuthMethodAttributes

        :param id: The ID of the auth method.
        :type id: str

        :param relationships: Relationships of a webhooks auth method to its protocol-specific resource.
        :type relationships: WebhooksAuthMethodRelationships, optional

        :param type: Webhooks auth method resource type.
        :type type: WebhooksAuthMethodType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
