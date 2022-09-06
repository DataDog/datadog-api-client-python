# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UserListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.user import User

        return {
            "users": ([User],),
        }

    attribute_map = {
        "users": "users",
    }

    def __init__(self_, *args, **kwargs):
        """
        Array of Datadog users for a given organization.

        :param users: Array of users.
        :type users: [User], optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
