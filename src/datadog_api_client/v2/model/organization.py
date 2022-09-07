# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class Organization(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.organization_attributes import OrganizationAttributes
        from datadog_api_client.v2.model.organizations_type import OrganizationsType

        return {
            "attributes": (OrganizationAttributes,),
            "id": (str,),
            "type": (OrganizationsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, type, *args, **kwargs):
        """
        Organization object.

        :param attributes: Attributes of the organization.
        :type attributes: OrganizationAttributes, optional

        :param id: ID of the organization.
        :type id: str, optional

        :param type: Organizations resource type.
        :type type: OrganizationsType
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.type = type
