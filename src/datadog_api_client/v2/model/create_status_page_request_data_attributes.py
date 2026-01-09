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
    from datadog_api_client.v2.model.create_status_page_request_data_attributes_components_items import (
        CreateStatusPageRequestDataAttributesComponentsItems,
    )
    from datadog_api_client.v2.model.create_status_page_request_data_attributes_type import (
        CreateStatusPageRequestDataAttributesType,
    )
    from datadog_api_client.v2.model.create_status_page_request_data_attributes_visualization_type import (
        CreateStatusPageRequestDataAttributesVisualizationType,
    )


class CreateStatusPageRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_status_page_request_data_attributes_components_items import (
            CreateStatusPageRequestDataAttributesComponentsItems,
        )
        from datadog_api_client.v2.model.create_status_page_request_data_attributes_type import (
            CreateStatusPageRequestDataAttributesType,
        )
        from datadog_api_client.v2.model.create_status_page_request_data_attributes_visualization_type import (
            CreateStatusPageRequestDataAttributesVisualizationType,
        )

        return {
            "company_logo": (str,),
            "components": ([CreateStatusPageRequestDataAttributesComponentsItems],),
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
        "components": "components",
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
        domain_prefix: str,
        enabled: bool,
        name: str,
        type: CreateStatusPageRequestDataAttributesType,
        visualization_type: CreateStatusPageRequestDataAttributesVisualizationType,
        company_logo: Union[str, UnsetType] = unset,
        components: Union[List[CreateStatusPageRequestDataAttributesComponentsItems], UnsetType] = unset,
        email_header_image: Union[str, UnsetType] = unset,
        favicon: Union[str, UnsetType] = unset,
        subscriptions_enabled: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param company_logo:
        :type company_logo: str, optional

        :param components:
        :type components: [CreateStatusPageRequestDataAttributesComponentsItems], optional

        :param domain_prefix:
        :type domain_prefix: str

        :param email_header_image:
        :type email_header_image: str, optional

        :param enabled:
        :type enabled: bool

        :param favicon:
        :type favicon: str, optional

        :param name:
        :type name: str

        :param subscriptions_enabled:
        :type subscriptions_enabled: bool, optional

        :param type:
        :type type: CreateStatusPageRequestDataAttributesType

        :param visualization_type:
        :type visualization_type: CreateStatusPageRequestDataAttributesVisualizationType
        """
        if company_logo is not unset:
            kwargs["company_logo"] = company_logo
        if components is not unset:
            kwargs["components"] = components
        if email_header_image is not unset:
            kwargs["email_header_image"] = email_header_image
        if favicon is not unset:
            kwargs["favicon"] = favicon
        if subscriptions_enabled is not unset:
            kwargs["subscriptions_enabled"] = subscriptions_enabled
        super().__init__(kwargs)

        self_.domain_prefix = domain_prefix
        self_.enabled = enabled
        self_.name = name
        self_.type = type
        self_.visualization_type = visualization_type
