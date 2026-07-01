# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class LogsArchiveIntegrationS3(ModelComposed):
    def __init__(self, **kwargs):
        """
        The S3 Archive's integration destination. You must provide one of the following: ``access_key_id`` alone, or both ``account_id`` and ``role_name`` together.

        :param access_key_id: The access key ID for the integration.
        :type access_key_id: str

        :param account_id: The account ID for the integration.
        :type account_id: str

        :param role_name: The name of the role to assume for the integration.
        :type role_name: str
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
        from datadog_api_client.v2.model.logs_archive_integration_s3_access_key import LogsArchiveIntegrationS3AccessKey
        from datadog_api_client.v2.model.logs_archive_integration_s3_role import LogsArchiveIntegrationS3Role

        return {
            "oneOf": [
                LogsArchiveIntegrationS3AccessKey,
                LogsArchiveIntegrationS3Role,
            ],
        }
