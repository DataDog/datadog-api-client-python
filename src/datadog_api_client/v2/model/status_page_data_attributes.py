# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.status_page_data_attributes_components_items import (
        StatusPageDataAttributesComponentsItems,
    )
    from datadog_api_client.v2.model.create_status_page_request_data_attributes_type import (
        CreateStatusPageRequestDataAttributesType,
    )
    from datadog_api_client.v2.model.create_status_page_request_data_attributes_visualization_type import (
        CreateStatusPageRequestDataAttributesVisualizationType,
    )


class StatusPageDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.status_page_data_attributes_components_items import (
            StatusPageDataAttributesComponentsItems,
        )
        from datadog_api_client.v2.model.create_status_page_request_data_attributes_type import (
            CreateStatusPageRequestDataAttributesType,
        )
        from datadog_api_client.v2.model.create_status_page_request_data_attributes_visualization_type import (
            CreateStatusPageRequestDataAttributesVisualizationType,
        )

        return {
            "company_logo": (str, none_type),
            "components": ([StatusPageDataAttributesComponentsItems],),
            "created_at": (datetime,),
            "custom_domain": (str, none_type),
            "custom_domain_enabled": (bool,),
            "domain_prefix": (str,),
            "email_header_image": (str, none_type),
            "enabled": (bool,),
            "favicon": (str, none_type),
            "modified_at": (datetime,),
            "name": (str,),
            "page_url": (str,),
            "subscriptions_enabled": (bool,),
            "type": (CreateStatusPageRequestDataAttributesType,),
            "visualization_type": (CreateStatusPageRequestDataAttributesVisualizationType,),
        }

    attribute_map = {
        "company_logo": "company_logo",
        "components": "components",
        "created_at": "created_at",
        "custom_domain": "custom_domain",
        "custom_domain_enabled": "custom_domain_enabled",
        "domain_prefix": "domain_prefix",
        "email_header_image": "email_header_image",
        "enabled": "enabled",
        "favicon": "favicon",
        "modified_at": "modified_at",
        "name": "name",
        "page_url": "page_url",
        "subscriptions_enabled": "subscriptions_enabled",
        "type": "type",
        "visualization_type": "visualization_type",
    }

    def __init__(
        self_,
        company_logo: Union[str, none_type, UnsetType] = unset,
        components: Union[List[StatusPageDataAttributesComponentsItems], UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        custom_domain: Union[str, none_type, UnsetType] = unset,
        custom_domain_enabled: Union[bool, UnsetType] = unset,
        domain_prefix: Union[str, UnsetType] = unset,
        email_header_image: Union[str, none_type, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        favicon: Union[str, none_type, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        page_url: Union[str, UnsetType] = unset,
        subscriptions_enabled: Union[bool, UnsetType] = unset,
        type: Union[CreateStatusPageRequestDataAttributesType, UnsetType] = unset,
        visualization_type: Union[CreateStatusPageRequestDataAttributesVisualizationType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of a status page.

        :param company_logo: Base64-encoded image data displayed on the status page.
        :type company_logo: str, none_type, optional

        :param components: Components displayed on the status page.
        :type components: [StatusPageDataAttributesComponentsItems], optional

        :param created_at: Timestamp of when the status page was created.
        :type created_at: datetime, optional

        :param custom_domain: If configured, the url that the status page is accessible at.
        :type custom_domain: str, none_type, optional

        :param custom_domain_enabled: Whether the custom domain is configured.
        :type custom_domain_enabled: bool, optional

        :param domain_prefix: The subdomain of the status page's url taking the form ``https://{domain_prefix}.statuspage.datadoghq.com``. Globally unique across Datadog Status Pages.
        :type domain_prefix: str, optional

        :param email_header_image: Base64-encoded image data included in email notifications sent to status page subscribers.
        :type email_header_image: str, none_type, optional

        :param enabled: Whether the status page is enabled.
        :type enabled: bool, optional

        :param favicon: Base64-encoded image data displayed in the browser tab.
        :type favicon: str, none_type, optional

        :param modified_at: Timestamp of when the status page was last modified.
        :type modified_at: datetime, optional

        :param name: The name of the status page.
        :type name: str, optional

        :param page_url: The url that the status page is accessible at.
        :type page_url: str, optional

        :param subscriptions_enabled: Whether users can subscribe to the status page.
        :type subscriptions_enabled: bool, optional

        :param type: The type of the status page controlling how the status page is accessed.
        :type type: CreateStatusPageRequestDataAttributesType, optional

        :param visualization_type: The visualization type of the status page.
        :type visualization_type: CreateStatusPageRequestDataAttributesVisualizationType, optional
        """
        if company_logo is not unset:
            kwargs["company_logo"] = company_logo
        if components is not unset:
            kwargs["components"] = components
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if custom_domain is not unset:
            kwargs["custom_domain"] = custom_domain
        if custom_domain_enabled is not unset:
            kwargs["custom_domain_enabled"] = custom_domain_enabled
        if domain_prefix is not unset:
            kwargs["domain_prefix"] = domain_prefix
        if email_header_image is not unset:
            kwargs["email_header_image"] = email_header_image
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if favicon is not unset:
            kwargs["favicon"] = favicon
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if name is not unset:
            kwargs["name"] = name
        if page_url is not unset:
            kwargs["page_url"] = page_url
        if subscriptions_enabled is not unset:
            kwargs["subscriptions_enabled"] = subscriptions_enabled
        if type is not unset:
            kwargs["type"] = type
        if visualization_type is not unset:
            kwargs["visualization_type"] = visualization_type
        super().__init__(kwargs)
