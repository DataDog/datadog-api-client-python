# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentNotificationHandle(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "display_name": (str,),
            "handle": (str,),
        }

    attribute_map = {
        "display_name": "display_name",
        "handle": "handle",
    }

    def __init__(self, *args, **kwargs):
        """
        A notification handle that will be notified at incident creation.

        :param display_name: The name of the notified handle.
        :type display_name: str, optional

        :param handle: The email address used for the notification.
        :type handle: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(IncidentNotificationHandle, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
