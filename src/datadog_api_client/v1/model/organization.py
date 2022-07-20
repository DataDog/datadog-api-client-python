# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class Organization(ModelNormal):
    validations = {
        "name": {
            "max_length": 32,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.organization_billing import OrganizationBilling
        from datadog_api_client.v1.model.organization_settings import OrganizationSettings
        from datadog_api_client.v1.model.organization_subscription import OrganizationSubscription

        return {
            "billing": (OrganizationBilling,),
            "created": (str,),
            "description": (str,),
            "name": (str,),
            "public_id": (str,),
            "settings": (OrganizationSettings,),
            "subscription": (OrganizationSubscription,),
            "trial": (bool,),
        }

    attribute_map = {
        "billing": "billing",
        "created": "created",
        "description": "description",
        "name": "name",
        "public_id": "public_id",
        "settings": "settings",
        "subscription": "subscription",
        "trial": "trial",
    }
    read_only_vars = {
        "created",
    }

    def __init__(self, *args, **kwargs):
        """
        Create, edit, and manage organizations.

        :param billing: A JSON array of billing type.
        :type billing: OrganizationBilling, optional

        :param created: Date of the organization creation.
        :type created: str, optional

        :param description: Description of the organization.
        :type description: str, optional

        :param name: The name of the new child-organization, limited to 32 characters.
        :type name: str, optional

        :param public_id: The ``public_id`` of the organization you are operating within.
        :type public_id: str, optional

        :param settings: A JSON array of settings.
        :type settings: OrganizationSettings, optional

        :param subscription: Subscription definition.
        :type subscription: OrganizationSubscription, optional

        :param trial: Only available for MSP customers. Allows child organizations to be created on a trial plan.
        :type trial: bool, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(Organization, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
