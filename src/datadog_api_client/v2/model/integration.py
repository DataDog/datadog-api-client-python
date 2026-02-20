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
    from datadog_api_client.v2.model.integration_attributes import IntegrationAttributes
    from datadog_api_client.v2.model.integration_links import IntegrationLinks
    from datadog_api_client.v2.model.integration_type import IntegrationType


class Integration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.integration_attributes import IntegrationAttributes
        from datadog_api_client.v2.model.integration_links import IntegrationLinks
        from datadog_api_client.v2.model.integration_type import IntegrationType

        return {
            "attributes": (IntegrationAttributes,),
            "id": (str,),
            "links": (IntegrationLinks,),
            "type": (IntegrationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "links": "links",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: IntegrationAttributes,
        id: str,
        type: IntegrationType,
        links: Union[IntegrationLinks, UnsetType] = unset,
        **kwargs,
    ):
        """
        Integration resource object.

        :param attributes: Attributes for an integration.
        :type attributes: IntegrationAttributes

        :param id: The unique identifier of the integration.
        :type id: str

        :param links: Links for the integration resource.
        :type links: IntegrationLinks, optional

        :param type: Integration resource type.
        :type type: IntegrationType
        """
        if links is not unset:
            kwargs["links"] = links
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
