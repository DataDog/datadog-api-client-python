# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class OrganizationSettingsSamlStrictMode(ModelNormal):
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
        Has one property enabled (boolean).

        :param enabled: Whether or not the SAML strict mode is enabled. If true, all users must log in with SAML.
            Learn more on the `SAML Strict documentation <https://docs.datadoghq.com/account_management/saml/#saml-strict>`_.
        :type enabled: bool, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
