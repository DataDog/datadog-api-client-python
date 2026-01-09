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
    from datadog_api_client.v2.model.create_status_page_request_data_attributes_type import (
        CreateStatusPageRequestDataAttributesType,
    )
    from datadog_api_client.v2.model.create_status_page_request_data_attributes_visualization_type import (
        CreateStatusPageRequestDataAttributesVisualizationType,
    )


class PatchStatusPageRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_status_page_request_data_attributes_type import (
            CreateStatusPageRequestDataAttributesType,
        )
        from datadog_api_client.v2.model.create_status_page_request_data_attributes_visualization_type import (
            CreateStatusPageRequestDataAttributesVisualizationType,
        )

        return {
            "company_logo": (str,),
            "domain_prefix": (str,),
            "email_header_image": (str,),
            "enabled": (bool,),
            "favicon": (str,),
            "name": (str,),
            "subscriptions_enabled": (bool,),
            "type": (CreateStatusPageRequestDataAttributesType,),
            "visualization_type": (CreateStatusPageRequestDataAttributesVisualizationType,),
        }

    attribute_map = {
        "company_logo": "company_logo",
        "domain_prefix": "domain_prefix",
        "email_header_image": "email_header_image",
        "enabled": "enabled",
        "favicon": "favicon",
        "name": "name",
        "subscriptions_enabled": "subscriptions_enabled",
        "type": "type",
        "visualization_type": "visualization_type",
    }

    def __init__(
        self_,
        company_logo: Union[str, UnsetType] = unset,
        domain_prefix: Union[str, UnsetType] = unset,
        email_header_image: Union[str, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        favicon: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        subscriptions_enabled: Union[bool, UnsetType] = unset,
        type: Union[CreateStatusPageRequestDataAttributesType, UnsetType] = unset,
        visualization_type: Union[CreateStatusPageRequestDataAttributesVisualizationType, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param company_logo:
        :type company_logo: str, optional

        :param domain_prefix:
        :type domain_prefix: str, optional

        :param email_header_image:
        :type email_header_image: str, optional

        :param enabled:
        :type enabled: bool, optional

        :param favicon:
        :type favicon: str, optional

        :param name:
        :type name: str, optional

        :param subscriptions_enabled:
        :type subscriptions_enabled: bool, optional

        :param type:
        :type type: CreateStatusPageRequestDataAttributesType, optional

        :param visualization_type:
        :type visualization_type: CreateStatusPageRequestDataAttributesVisualizationType, optional
        """
        if company_logo is not unset:
            kwargs["company_logo"] = company_logo
        if domain_prefix is not unset:
            kwargs["domain_prefix"] = domain_prefix
        if email_header_image is not unset:
            kwargs["email_header_image"] = email_header_image
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if favicon is not unset:
            kwargs["favicon"] = favicon
        if name is not unset:
            kwargs["name"] = name
        if subscriptions_enabled is not unset:
            kwargs["subscriptions_enabled"] = subscriptions_enabled
        if type is not unset:
            kwargs["type"] = type
        if visualization_type is not unset:
            kwargs["visualization_type"] = visualization_type
        super().__init__(kwargs)
