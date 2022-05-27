# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ApplicationKeyListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.application_key import ApplicationKey

        return {
            "application_keys": ([ApplicationKey],),
        }

    attribute_map = {
        "application_keys": "application_keys",
    }

    def __init__(self, *args, **kwargs):
        """
        An application key response.

        :param application_keys: Array of application keys.
        :type application_keys: [ApplicationKey], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ApplicationKeyListResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
