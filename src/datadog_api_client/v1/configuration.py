# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.

from datadog_api_client.configuration import BaseConfiguration


class Configuration(BaseConfiguration):
    def __init__(
        self,
        host=None,
        api_key=None,
        api_key_prefix=None,
        access_token=None,
        username=None,
        password=None,
        discard_unknown_keys=True,
        disabled_client_side_validations="",
        server_index=None,
        server_variables=None,
        server_operation_index=None,
        server_operation_variables=None,
        ssl_ca_cert=None,
        compress=True,
    ):
        super(Configuration, self).__init__(
            host,
            api_key,
            api_key_prefix,
            access_token,
            username,
            password,
            discard_unknown_keys,
            disabled_client_side_validations,
            server_index,
            server_variables,
            server_operation_index,
            server_operation_variables,
            ssl_ca_cert,
            compress,
        )

        # Keep track of unstable operations
        self.unstable_operations = {
            "get_daily_custom_reports": False,
            "get_hourly_usage_attribution": False,
            "get_monthly_custom_reports": False,
            "get_monthly_usage_attribution": False,
            "get_specified_daily_custom_reports": False,
            "get_specified_monthly_custom_reports": False,
            "get_usage_attribution": False,
            "get_slo_corrections": False,
            "get_slo_history": False,
            "create_slo_correction": False,
            "delete_slo_correction": False,
            "get_slo_correction": False,
            "list_slo_correction": False,
            "update_slo_correction": False,
        }
