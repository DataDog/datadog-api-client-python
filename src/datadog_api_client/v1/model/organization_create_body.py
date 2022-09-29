# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class OrganizationCreateBody(ModelNormal):
    validations = {
        "name": {
            "max_length": 32,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.organization_billing import OrganizationBilling
        from datadog_api_client.v1.model.organization_subscription import OrganizationSubscription

        return {
            "billing": (OrganizationBilling,),
            "name": (str,),
            "subscription": (OrganizationSubscription,),
        }

    attribute_map = {
        "billing": "billing",
        "name": "name",
        "subscription": "subscription",
    }

    def __init__(self_, name, *args, **kwargs):
        """
        Object describing an organization to create.

        :param billing: A JSON array of billing type. **Deprecated**.
        :type billing: OrganizationBilling, optional

        :param name: The name of the new child-organization, limited to 32 characters.
        :type name: str

        :param subscription: Subscription definition. **Deprecated**.
        :type subscription: OrganizationSubscription, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.name = name
