# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    date,
    datetime,
    file_type,
    none_type,
)


def lazy_import():
    from datadog_api_client.v1.model.synthetics_api_test_result_short import SyntheticsAPITestResultShort

    globals()["SyntheticsAPITestResultShort"] = SyntheticsAPITestResultShort


class SyntheticsGetAPITestLatestResultsResponse(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "last_timestamp_fetched": (int,),
            "results": ([SyntheticsAPITestResultShort],),
        }

    attribute_map = {
        "last_timestamp_fetched": "last_timestamp_fetched",
        "results": "results",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """SyntheticsGetAPITestLatestResultsResponse - a model defined in OpenAPI

        Keyword Args:
            last_timestamp_fetched (int): [optional] Timestamp of the latest API test run.
            results ([SyntheticsAPITestResultShort]): [optional] Result of the latest API test run.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsGetAPITestLatestResultsResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
