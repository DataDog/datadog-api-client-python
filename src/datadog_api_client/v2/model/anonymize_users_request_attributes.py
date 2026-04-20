# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AnonymizeUsersRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "user_ids": ([str],),
        }

    attribute_map = {
        "user_ids": "user_ids",
    }

    def __init__(self_, user_ids: List[str], **kwargs):
        """
        Attributes of an anonymize users request.

        :param user_ids: List of user IDs (UUIDs) to anonymize.
        :type user_ids: [str]
        """
        super().__init__(kwargs)

        self_.user_ids = user_ids
