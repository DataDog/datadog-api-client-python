# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.access_role import AccessRole
    from datadog_api_client.v1.model.organization_settings_saml import OrganizationSettingsSaml
    from datadog_api_client.v1.model.organization_settings_saml_autocreate_users_domains import (
        OrganizationSettingsSamlAutocreateUsersDomains,
    )
    from datadog_api_client.v1.model.organization_settings_saml_idp_initiated_login import (
        OrganizationSettingsSamlIdpInitiatedLogin,
    )
    from datadog_api_client.v1.model.organization_settings_saml_strict_mode import OrganizationSettingsSamlStrictMode

    globals()["AccessRole"] = AccessRole
    globals()["OrganizationSettingsSaml"] = OrganizationSettingsSaml
    globals()["OrganizationSettingsSamlAutocreateUsersDomains"] = OrganizationSettingsSamlAutocreateUsersDomains
    globals()["OrganizationSettingsSamlIdpInitiatedLogin"] = OrganizationSettingsSamlIdpInitiatedLogin
    globals()["OrganizationSettingsSamlStrictMode"] = OrganizationSettingsSamlStrictMode


class OrganizationSettings(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "private_widget_share": (bool,),
            "saml": (OrganizationSettingsSaml,),
            "saml_autocreate_access_role": (AccessRole,),
            "saml_autocreate_users_domains": (OrganizationSettingsSamlAutocreateUsersDomains,),
            "saml_can_be_enabled": (bool,),
            "saml_idp_endpoint": (str,),
            "saml_idp_initiated_login": (OrganizationSettingsSamlIdpInitiatedLogin,),
            "saml_idp_metadata_uploaded": (bool,),
            "saml_login_url": (str,),
            "saml_strict_mode": (OrganizationSettingsSamlStrictMode,),
        }

    attribute_map = {
        "private_widget_share": "private_widget_share",
        "saml": "saml",
        "saml_autocreate_access_role": "saml_autocreate_access_role",
        "saml_autocreate_users_domains": "saml_autocreate_users_domains",
        "saml_can_be_enabled": "saml_can_be_enabled",
        "saml_idp_endpoint": "saml_idp_endpoint",
        "saml_idp_initiated_login": "saml_idp_initiated_login",
        "saml_idp_metadata_uploaded": "saml_idp_metadata_uploaded",
        "saml_login_url": "saml_login_url",
        "saml_strict_mode": "saml_strict_mode",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """OrganizationSettings - a model defined in OpenAPI


        :param private_widget_share: Whether or not the organization users can share widgets outside of Datadog.
        :type private_widget_share: bool, optional

        :type saml: OrganizationSettingsSaml, optional

        :type saml_autocreate_access_role: AccessRole, optional

        :type saml_autocreate_users_domains: OrganizationSettingsSamlAutocreateUsersDomains, optional

        :param saml_can_be_enabled: Whether or not SAML can be enabled for this organization.
        :type saml_can_be_enabled: bool, optional

        :param saml_idp_endpoint: Identity provider endpoint for SAML authentication.
        :type saml_idp_endpoint: str, optional

        :type saml_idp_initiated_login: OrganizationSettingsSamlIdpInitiatedLogin, optional

        :param saml_idp_metadata_uploaded: Whether or not a SAML identity provider metadata file was provided to the Datadog organization.
        :type saml_idp_metadata_uploaded: bool, optional

        :param saml_login_url: URL for SAML logging.
        :type saml_login_url: str, optional

        :type saml_strict_mode: OrganizationSettingsSamlStrictMode, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(OrganizationSettings, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
