# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class OrganizationSettingsSamlAutocreateUsersDomains(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "domains": ([str],),
            "enabled": (bool,),
        }

    attribute_map = {
        "domains": "domains",
        "enabled": "enabled",
    }

    def __init__(self, *args, **kwargs):
        """
        Has two properties, ``enabled`` (boolean) and ``domains`` , which is a list of domains without the @ symbol.

        :param domains: List of domains where the SAML automated user creation is enabled.
        :type domains: [str], optional

        :param enabled: Whether or not the automated user creation based on SAML domain is enabled.
        :type enabled: bool, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(OrganizationSettingsSamlAutocreateUsersDomains, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
