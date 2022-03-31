# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class OrganizationAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "description": (str,),
            "disabled": (bool,),
            "modified_at": (datetime,),
            "name": (str,),
            "public_id": (str,),
            "sharing": (str,),
            "url": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "description": "description",
        "disabled": "disabled",
        "modified_at": "modified_at",
        "name": "name",
        "public_id": "public_id",
        "sharing": "sharing",
        "url": "url",
    }

    def __init__(self, *args, **kwargs):
        """
        Attributes of the organization.

        :param created_at: Creation time of the organization.
        :type created_at: datetime, optional

        :param description: Description of the organization.
        :type description: str, optional

        :param disabled: Whether or not the organization is disabled.
        :type disabled: bool, optional

        :param modified_at: Time of last organization modification.
        :type modified_at: datetime, optional

        :param name: Name of the organization.
        :type name: str, optional

        :param public_id: Public ID of the organization.
        :type public_id: str, optional

        :param sharing: Sharing type of the organization.
        :type sharing: str, optional

        :param url: URL of the site that this organization exists at.
        :type url: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(OrganizationAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
