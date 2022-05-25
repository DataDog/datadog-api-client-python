# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsBrowserTestRumSettings(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "application_id": (str,),
            "client_token_id": (int,),
            "is_enabled": (bool,),
        }

    attribute_map = {
        "application_id": "applicationId",
        "client_token_id": "clientTokenId",
        "is_enabled": "isEnabled",
    }

    def __init__(self, is_enabled, *args, **kwargs):
        """
        The RUM data collection settings for the Synthetic browser test.
        **Note:** There are 3 ways to format RUM settings:

        ``{ isEnabled: false }``
        RUM data is not collected.

        ``{ isEnabled: true }``
        RUM data is collected from the Synthetic test's default application.

        ``{ isEnabled: true, applicationId: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", clientTokenId: 12345 }``
        RUM data is collected using the specified application.

        :param application_id: RUM application ID used to collect RUM data for the browser test.
        :type application_id: str, optional

        :param client_token_id: RUM application API key ID used to collect RUM data for the browser test.
        :type client_token_id: int, optional

        :param is_enabled: Determines whether RUM data is collected during test runs.
        :type is_enabled: bool
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.is_enabled = is_enabled

    @classmethod
    def _from_openapi_data(cls, is_enabled, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsBrowserTestRumSettings, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.is_enabled = is_enabled
        return self
