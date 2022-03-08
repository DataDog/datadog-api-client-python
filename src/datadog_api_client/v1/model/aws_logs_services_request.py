# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AWSLogsServicesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "account_id": (str,),
            "services": ([str],),
        }

    attribute_map = {
        "account_id": "account_id",
        "services": "services",
    }

    def __init__(self, account_id, services, *args, **kwargs):
        """
        A list of current AWS services for which Datadog offers automatic log collection.

        :param account_id: Your AWS Account ID without dashes.
        :type account_id: str

        :param services: Array of services IDs set to enable automatic log collection. Discover the list of available services with the get list of AWS log ready services API endpoint.
        :type services: [str]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.account_id = account_id
        self.services = services

    @classmethod
    def _from_openapi_data(cls, account_id, services, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(AWSLogsServicesRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.account_id = account_id
        self.services = services
        return self
