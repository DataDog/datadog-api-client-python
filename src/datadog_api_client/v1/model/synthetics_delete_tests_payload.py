# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsDeleteTestsPayload(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "public_ids": ([str],),
        }

    attribute_map = {
        "public_ids": "public_ids",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """SyntheticsDeleteTestsPayload - a model defined in OpenAPI


        :param public_ids: An array of Synthetic test IDs you want to delete.
        :type public_ids: [str], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsDeleteTestsPayload, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
