def test_version():
    from datadog_api_client.version import __version__

    assert __version__
