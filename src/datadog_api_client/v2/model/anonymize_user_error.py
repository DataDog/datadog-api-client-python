# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AnonymizeUserError(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "error": (str,),
            "user_id": (str,),
        }

    attribute_map = {
        "error": "error",
        "user_id": "user_id",
    }

    def __init__(self_, error: str, user_id: str, **kwargs):
        """
        Error encountered when anonymizing a specific user.

        :param error: Error message describing why anonymization failed.
        :type error: str

        :param user_id: UUID of the user that failed to be anonymized.
        :type user_id: str
        """
        super().__init__(kwargs)

        self_.error = error
        self_.user_id = user_id
