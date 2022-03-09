# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UserUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "disabled": (bool,),
            "email": (str,),
            "name": (str,),
        }

    attribute_map = {
        "disabled": "disabled",
        "email": "email",
        "name": "name",
    }

    def __init__(self, *args, **kwargs):
        """
        Attributes of the edited user.

        :param disabled: If the user is enabled or disabled.
        :type disabled: bool, optional

        :param email: The email of the user.
        :type email: str, optional

        :param name: The name of the user.
        :type name: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UserUpdateAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
