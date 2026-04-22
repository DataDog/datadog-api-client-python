# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.anonymize_user_error import AnonymizeUserError


class AnonymizeUsersResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.anonymize_user_error import AnonymizeUserError

        return {
            "anonymize_errors": ([AnonymizeUserError],),
            "anonymized_user_ids": ([str],),
        }

    attribute_map = {
        "anonymize_errors": "anonymize_errors",
        "anonymized_user_ids": "anonymized_user_ids",
    }

    def __init__(self_, anonymize_errors: List[AnonymizeUserError], anonymized_user_ids: List[str], **kwargs):
        """
        Attributes of an anonymize users response.

        :param anonymize_errors: List of errors encountered during anonymization, one entry per failed user.
        :type anonymize_errors: [AnonymizeUserError]

        :param anonymized_user_ids: List of user IDs (UUIDs) that were successfully anonymized.
        :type anonymized_user_ids: [str]
        """
        super().__init__(kwargs)

        self_.anonymize_errors = anonymize_errors
        self_.anonymized_user_ids = anonymized_user_ids
