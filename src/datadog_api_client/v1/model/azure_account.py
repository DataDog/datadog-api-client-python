# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AzureAccount(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "automute": (bool,),
            "client_id": (str,),
            "client_secret": (str,),
            "errors": ([str],),
            "host_filters": (str,),
            "new_client_id": (str,),
            "new_tenant_name": (str,),
            "tenant_name": (str,),
        }

    attribute_map = {
        "automute": "automute",
        "client_id": "client_id",
        "client_secret": "client_secret",
        "errors": "errors",
        "host_filters": "host_filters",
        "new_client_id": "new_client_id",
        "new_tenant_name": "new_tenant_name",
        "tenant_name": "tenant_name",
    }

    def __init__(self, *args, **kwargs):
        """
        Datadog-Azure integrations configured for your organization.

        :param automute: Silence monitors for expected Azure VM shutdowns.
        :type automute: bool, optional

        :param client_id: Your Azure web application ID.
        :type client_id: str, optional

        :param client_secret: Your Azure web application secret key.
        :type client_secret: str, optional

        :param errors: Errors in your configuration.
        :type errors: [str], optional

        :param host_filters: Limit the Azure instances that are pulled into Datadog by using tags.
            Only hosts that match one of the defined tags are imported into Datadog.
        :type host_filters: str, optional

        :param new_client_id: Your New Azure web application ID.
        :type new_client_id: str, optional

        :param new_tenant_name: Your New Azure Active Directory ID.
        :type new_tenant_name: str, optional

        :param tenant_name: Your Azure Active Directory ID.
        :type tenant_name: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(AzureAccount, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
