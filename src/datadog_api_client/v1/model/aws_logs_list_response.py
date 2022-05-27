# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AWSLogsListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.aws_logs_lambda import AWSLogsLambda

        return {
            "account_id": (str,),
            "lambdas": ([AWSLogsLambda],),
            "services": ([str],),
        }

    attribute_map = {
        "account_id": "account_id",
        "lambdas": "lambdas",
        "services": "services",
    }

    def __init__(self, *args, **kwargs):
        """
        A list of all Datadog-AWS logs integrations available in your Datadog organization.

        :param account_id: Your AWS Account ID without dashes.
        :type account_id: str, optional

        :param lambdas: List of ARNs configured in your Datadog account.
        :type lambdas: [AWSLogsLambda], optional

        :param services: Array of services IDs.
        :type services: [str], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(AWSLogsListResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
