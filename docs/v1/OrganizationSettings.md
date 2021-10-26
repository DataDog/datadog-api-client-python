# OrganizationSettings

A JSON array of settings.

## Properties

| Name                              | Type                                                                                                    | Description                                                                                     | Notes      |
| --------------------------------- | ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ---------- |
| **private_widget_share**          | **bool**                                                                                                | Whether or not the organization users can share widgets outside of Datadog.                     | [optional] |
| **saml**                          | [**OrganizationSettingsSaml**](OrganizationSettingsSaml.md)                                             |                                                                                                 | [optional] |
| **saml_autocreate_access_role**   | [**AccessRole**](AccessRole.md)                                                                         |                                                                                                 | [optional] |
| **saml_autocreate_users_domains** | [**OrganizationSettingsSamlAutocreateUsersDomains**](OrganizationSettingsSamlAutocreateUsersDomains.md) |                                                                                                 | [optional] |
| **saml_can_be_enabled**           | **bool**                                                                                                | Whether or not SAML can be enabled for this organization.                                       | [optional] |
| **saml_idp_endpoint**             | **str**                                                                                                 | Identity provider endpoint for SAML authentication.                                             | [optional] |
| **saml_idp_initiated_login**      | [**OrganizationSettingsSamlIdpInitiatedLogin**](OrganizationSettingsSamlIdpInitiatedLogin.md)           |                                                                                                 | [optional] |
| **saml_idp_metadata_uploaded**    | **bool**                                                                                                | Whether or not a SAML identity provider metadata file was provided to the Datadog organization. | [optional] |
| **saml_login_url**                | **str**                                                                                                 | URL for SAML logging.                                                                           | [optional] |
| **saml_strict_mode**              | [**OrganizationSettingsSamlStrictMode**](OrganizationSettingsSamlStrictMode.md)                         |                                                                                                 | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
