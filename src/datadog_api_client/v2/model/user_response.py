# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.user import User
    from datadog_api_client.v2.model.user_response_included_item import UserResponseIncludedItem

    globals()["User"] = User
    globals()["UserResponseIncludedItem"] = UserResponseIncludedItem


class UserResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        lazy_import()
        return {
            "data": (User,),
            "included": ([UserResponseIncludedItem],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(self, *args, **kwargs):
        """
        Response containing information about a single user.

        :param data: User object returned by the API.
        :type data: User, optional

        :param included: Array of objects related to the user.
        :type included: [UserResponseIncludedItem], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UserResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
