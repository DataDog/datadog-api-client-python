# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class OrganizationCreateResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.api_key import ApiKey
        from datadog_api_client.v1.model.application_key import ApplicationKey
        from datadog_api_client.v1.model.organization import Organization
        from datadog_api_client.v1.model.user import User

        return {
            "api_key": (ApiKey,),
            "application_key": (ApplicationKey,),
            "org": (Organization,),
            "user": (User,),
        }

    attribute_map = {
        "api_key": "api_key",
        "application_key": "application_key",
        "org": "org",
        "user": "user",
    }

    def __init__(self, *args, **kwargs):
        """
        Response object for an organization creation.

        :param api_key: Datadog API key.
        :type api_key: ApiKey, optional

        :param application_key: An application key with its associated metadata.
        :type application_key: ApplicationKey, optional

        :param org: Create, edit, and manage organizations.
        :type org: Organization, optional

        :param user: Create, edit, and disable users.
        :type user: User, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(OrganizationCreateResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
