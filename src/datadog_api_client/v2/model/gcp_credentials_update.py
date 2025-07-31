# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class GCPCredentialsUpdate(ModelComposed):
    def __init__(self, **kwargs):
        """
        The definition of the ``GCPCredentialsUpdate`` object.

        :param private_key: The `GCPServiceAccountUpdate` `private_key`.
        :type private_key: str, optional

        :param service_account_email: The `GCPServiceAccountUpdate` `service_account_email`.
        :type service_account_email: str, optional

        :param type: The definition of the `GCPServiceAccount` object.
        :type type: GCPServiceAccountCredentialType
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.gcp_service_account_update import GCPServiceAccountUpdate

        return {
            "oneOf": [
                GCPServiceAccountUpdate,
            ],
        }
