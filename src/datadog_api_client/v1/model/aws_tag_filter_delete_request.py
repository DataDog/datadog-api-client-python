# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AWSTagFilterDeleteRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.aws_namespace import AWSNamespace

        return {
            "account_id": (str,),
            "namespace": (AWSNamespace,),
        }

    attribute_map = {
        "account_id": "account_id",
        "namespace": "namespace",
    }

    def __init__(self, *args, **kwargs):
        """
        The objects used to delete an AWS tag filter entry.

        :param account_id: The unique identifier of your AWS account.
        :type account_id: str, optional

        :param namespace: The namespace associated with the tag filter entry.
        :type namespace: AWSNamespace, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(AWSTagFilterDeleteRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
