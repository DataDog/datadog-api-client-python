# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsArchiveIntegrationGCS(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "client_email": (str,),
            "project_id": (str,),
        }

    attribute_map = {
        "client_email": "client_email",
        "project_id": "project_id",
    }

    def __init__(self, client_email, project_id, *args, **kwargs):
        """
        The GCS archive's integration destination.

        :param client_email: A client email.
        :type client_email: str

        :param project_id: A project ID.
        :type project_id: str
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.client_email = client_email
        self.project_id = project_id

    @classmethod
    def _from_openapi_data(cls, client_email, project_id, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsArchiveIntegrationGCS, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.client_email = client_email
        self.project_id = project_id
        return self
