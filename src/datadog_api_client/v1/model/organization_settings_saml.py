# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class OrganizationSettingsSaml(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "enabled": (bool,),
        }

    attribute_map = {
        "enabled": "enabled",
    }

    def __init__(self_, *args, **kwargs):
        """
        Set the boolean property enabled to enable or disable single sign on with SAML.
        See the SAML documentation for more information about all SAML settings.

        :param enabled: Whether or not SAML is enabled for this organization.
        :type enabled: bool, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
